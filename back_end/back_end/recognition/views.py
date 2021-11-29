from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Image
import base64
from django.core.files.base import ContentFile
import json
from .tasks import recognize_image


# Create your views here.


# TODO: Fill in two view functions below.
from back_end.settings import BASE_DIR


def upload_image(request):
    """
    Receive an image uploaded from the browser, save it to the disk, and create a record in the database. Then,
    create a task in the task queue. Return uuid if succeed. :param request: :return: JsonResponse
    """

    if request.method == 'POST':
        new_img = Image(
            status=Image.TaskStatus.WAITING,
        )
        new_img.save()
        json_data = json.loads(request.body.decode('utf-8'))
        ext, img_binary = get_img(json_data['image_b64'])
        new_img.image.save(f'{new_img.uuid}.{ext}', ContentFile(img_binary))

        new_img.save()

        # TODO add task to celery

        recognize_image.delay(img_binary)

        return JsonResponse({
            'code': 0,
            'message': 'OK',
            'result': {
                'uuid': new_img.uuid
            }
        })
    else:
        return JsonResponse({
            'code': 1,
            'message': 'Request passed to upload is not POST ',
            'result': {
                'uuid': ''
            }
        })


def get_img(data):
    extend, img_str = data.split(';base64,')
    ext = extend.split('/')[-1]
    return ext, base64.b64decode(img_str)
    # return ContentFile(base64.b64decode(img_str), name=uuid + '.' + ext)



def query_result(request, uuid_req):
    """
    Query the recognition result of an image specified by uuid. If the uuid does not exist, return error.
    :param request:
    :return: JsonResponse
    """
    if request.method == 'GET':
        try:
            img_record = Image.objects.get(uuid=uuid_req)
        except Image.DoesNotExist:
            return JsonResponse({
                'code': 1,
                'result': {
                    'uuid': uuid_req,
                    'status': 0,
                }
            })
        img_name = img_record.image.name
        img_url = BASE_DIR / 'media' + img_name
        return JsonResponse({
            'code': 0,
            'result': {
                'uuid': uuid_req,
                'img_url': img_url,
                'status': img_record.status,
                'category': img_record.category,
                'probability': img_record.probability,
            }
        })
    else:
        return JsonResponse({
            'code': 1,
            'message': 'Request passed to upload is not GET ',
            'result': {
                'uuid': uuid_req,
                'status': 0,
            }
        })


def update_result(request, uuid_req):
    '''
    An interface for celery worker to return the results to.
    :param request:
    :param uuid:
    :return:
    '''

    if request.method == 'POST':
        try:
            img_record = Image.objects.get(uuid=uuid_req)
        except Image.DoesNotExist:
            return JsonResponse({
                'code': 1,
                'result': {
                    'uuid': uuid_req,
                    'status': 0,
                }
            })

        json_data = json.loads(request.body.decode('utf-8'))

        img_record.status = json_data['status']

        if json_data['status'] == Image.TaskStatus.COMPLETED.value:
            img_record.category = json_data['category']
            img_record.probability = json_data['probability']


        return JsonResponse({
            'code':0,
            'message': 'OK',
            'result': None,
        })

    else:
        return JsonResponse({
            'code': 1,
            'message': 'Request passed to update is not POST ',
            'result': {
                'uuid': ''
            }
        })
