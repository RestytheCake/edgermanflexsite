# Generated by Django 3.1.7 on 2021-03-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0010_auto_20210312_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='main_post',
            new_name='main_post_user',
        ),
        migrations.AddField(
            model_name='comment',
            name='main_post_title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
