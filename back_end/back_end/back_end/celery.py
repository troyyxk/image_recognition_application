import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back_end.settings')

app = Celery('back_end', broker=os.getenv('amqp://guest@localhost:5672//'))
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')