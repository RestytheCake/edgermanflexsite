# Generated by Django 3.1.7 on 2021-03-12 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0011_auto_20210312_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='comments',
        ),
    ]