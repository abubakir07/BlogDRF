# Generated by Django 4.1.5 on 2023-01-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('image', models.ImageField(max_length=256, upload_to='post_images/', verbose_name='image')),
                ('description', models.TextField(verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creted_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
