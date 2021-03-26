# Generated by Django 3.1.7 on 2021-03-26 19:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0004_auto_20210326_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fa_send',
            field=models.ManyToManyField(blank=True, related_name='fa_send', to=settings.AUTH_USER_MODEL),
        ),
    ]
