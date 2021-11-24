from django.db import models

import uuid

# Create your models here.

class Image(models.Model):

    class TaskStatus(models.IntegerChoices):
        WAITING = 1
        RUNNING = 2
        COMPLETED = 3
        FAILED = -1


    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images')
    status = models.IntegerField(choices=TaskStatus.choices)
    category = models.CharField(max_length=128, blank=True, help_text='This is the category with highest probability.')
    probability = models.DecimalField(max_digits=8, default=0.0, decimal_places=3)
    raw_output = models.TextField(blank=True, help_text='The raw output (with all possible categories) returned by GoogleNet.')


    def __str__(self):
        return f'[{self.uuid.hex[0:8]}]'
