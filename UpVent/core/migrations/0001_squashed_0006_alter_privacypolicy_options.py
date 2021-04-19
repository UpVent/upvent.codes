# Generated by Django 3.2 on 2021-04-17 00:17

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('core', '0001_initial'), ('core', '0002_alter_project_site'), ('core', '0003_auto_20210409_1723'), ('core', '0004_privacypolicy'), ('core', '0005_alter_privacypolicy_title'), ('core', '0006_alter_privacypolicy_options')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Ingrese el nombre del proyecto', max_length=200, unique=True, verbose_name='Título')),
                ('image', models.ImageField(help_text='Se recomiendan imágenes de dimensiones rectangulares. Solo formatos jpg, jpeg, png y webm', upload_to='portfolio', verbose_name='Imágen Destacada')),
                ('site', models.URLField(help_text='El sitio web donde se encuentra alojado el proyecto', verbose_name='Sitio web')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(help_text='Descripción del proyecto. Procure ser breve.', verbose_name='Descripción')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
            },
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Política de Privacidad', help_text='Ingrese el título para su política de privacidad', max_length=100, verbose_name='Título')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now_add=True)),
                ('changelog', models.TextField(help_text='Ingrese la razón de cambiar la política de privacidad.', verbose_name='Registro de Cambios')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(help_text='Escriba aquí su política de privacidad', verbose_name='Política de privacidad')),
            ],
            options={
                'verbose_name': 'Política de Privacidad',
                'verbose_name_plural': 'Política de Privacidad',
            },
        ),
    ]