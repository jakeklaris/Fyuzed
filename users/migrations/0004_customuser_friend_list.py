# Generated by Django 3.0.6 on 2020-07-13 19:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200629_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='friend_list',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
