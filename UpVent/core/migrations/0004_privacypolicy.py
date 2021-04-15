# Generated by Django 3.2 on 2021-04-15 07:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210409_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Ingrese el título para su política de privacidad', max_length=100, verbose_name='Título')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now_add=True)),
                ('changelog', models.TextField(help_text='Ingrese la razón de cambiar la política de privacidad.', verbose_name='Registro de Cambios')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(help_text='Escriba aquí su política de privacidad', verbose_name='Política de privacidad')),
            ],
            options={
                'verbose_name': 'Política de Privacidad',
            },
        ),
    ]
