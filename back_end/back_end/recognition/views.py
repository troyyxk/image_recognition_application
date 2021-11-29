from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Image
import base64
from django.core.files.base import ContentFile


# Create your views here.


# TODO: Fill in two view functions below.
from ..back_end.settings import BASE_DIR


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
        data = request.FILES.get('Payload')
        img = get_img(data, new_img.uuid)
        new_img.image = img
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


def get_img(data, uuid):
    extend, img_str = data.split(';base64,')
    ext = extend.split('/')[-1]
    return ContentFile(base64.b64decode(img_str), name=uuid + '.' + ext)


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

