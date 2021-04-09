# Generated by Django 3.2 on 2021-04-09 07:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Título')),
                ('image', models.ImageField(upload_to='portfolio', verbose_name='Imágen Destacada')),
                ('site', models.CharField(max_length=200, verbose_name='Sitio web')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Descripción')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
