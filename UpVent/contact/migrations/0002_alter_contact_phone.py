# Generated by Django 3.2 on 2021-05-04 00:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', help_text='Ingrese el número de teléfono de la persona que nos        contactó', max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format:        '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Número de Teléfono'),
        ),
    ]
