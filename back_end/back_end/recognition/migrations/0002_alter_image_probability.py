# Generated by Django 3.2.9 on 2021-11-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='probability',
            field=models.DecimalField(decimal_places=3, default=0.0, max_digits=8),
        ),
    ]
