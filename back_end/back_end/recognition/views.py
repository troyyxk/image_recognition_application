from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


# TODO: Fill in two view functions below.

def upload_image(request):
    '''
    Receive an image uploaded from the browser, save it to the disk, and create a record in the database. Then, create a task in the task queue. Return uuid if succeed.
    :param request:
    :return: JsonResponse
    '''

    # TODO 1

    return JsonResponse({
        'code': 0,
        'message': 'OK',
        'result': {
            'uuid': ''
        }
    })


def query_result(request):
    '''
    Query the recognition result of an image specified by uuid. If the uuid does not exist, return error.
    :param request:
    :return: JsonResponse
    '''
    # TODO 2

    return JsonResponse({
        'code': 0,
        'result': {
            'uuid': 'xxx-xxx',
            'status': 0,

        }
    })