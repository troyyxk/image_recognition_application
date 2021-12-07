import torch
model = torch.hub.load('pytorch/vision:v0.10.0', 'googlenet', pretrained=True)
model.eval()

from celery import Celery, shared_task
import time
import requests

from PIL import Image
from torchvision import transforms
import io


app = Celery('tasks', broker='pyamqp://guest@server//')
app.conf.update(
    enable_utc=True,
    timezone='America/New_York',
    accept_content=['pickle'],
    task_serializer='pickle',
)

@shared_task(name='recognize_image')
def recognize_image(image_binary, uuid):
    session = requests.Session()
    res = session.post(f'http://server:28000/api/update/{uuid}/', json={'status': 1})
    print('received', uuid)

    input_image = Image.open(io.BytesIO(image_binary))
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(input_image)
    input_batch = input_tensor.unsqueeze(0)  # create a mini-batch as expected by the model

    # move the input and model to GPU for speed if available
    if torch.cuda.is_available():
        input_batch = input_batch.to('cuda')
        model.to('cuda')

    with torch.no_grad():
        output = model(input_batch)
    # Tensor of shape 1000, with confidence scores over Imagenet's 1000 classes
    print(output[0])
    # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    print(probabilities)

    # Read the categories
    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]
    # Show top categories per image
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    for i in range(top5_prob.size(0)):
        print(categories[top5_catid[i]], top5_prob[i].item())

    print('finished')
    res = session.post(
        f'http://server:28000/api/update/{uuid}/',
        json={
            'status': 2,
            'category': categories[top5_catid[0]],
            'probability': top5_prob[0].item()
        }
    )

    return 'OK'
