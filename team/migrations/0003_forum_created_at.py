# Generated by Django 3.1.7 on 2021-03-08 12:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20210308_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
