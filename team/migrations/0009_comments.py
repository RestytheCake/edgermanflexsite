# Generated by Django 3.1.7 on 2021-03-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0008_auto_20210310_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User', models.CharField(blank=True, max_length=255)),
                ('main_post', models.CharField(blank=True, max_length=255)),
                ('comment', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]