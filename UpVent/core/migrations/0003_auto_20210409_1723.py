# Generated by Django 3.2 on 2021-04-09 22:23

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_project_site'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created_on'], 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Descripción del proyecto. Procure ser breve.', verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(help_text='Se recomiendan imágenes de dimensiones rectangulares. Solo formatos jpg, jpeg, png y webm', upload_to='portfolio', verbose_name='Imágen Destacada'),
        ),
        migrations.AlterField(
            model_name='project',
            name='site',
            field=models.URLField(help_text='El sitio web donde se encuentra alojado el proyecto', verbose_name='Sitio web'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(help_text='Ingrese el nombre del proyecto', max_length=200, unique=True, verbose_name='Título'),
        ),
    ]
