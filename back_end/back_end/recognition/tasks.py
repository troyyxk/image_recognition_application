from celery import shared_task

@shared_task(name='recognize_image')
def recognize_image(image_binary):
    '''
    This is a dummy function. It will not be executed, instead the worker nodes will do the job.
    The definition here is to help django discover this function.
    :param image_binary:
    :return:
    '''

    return
