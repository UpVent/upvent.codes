# Generated by Django 3.2 on 2021-04-18 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210417_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fsproject',
            options={'verbose_name': 'Proyecto de código abierto', 'verbose_name_plural': 'Proyectos de código abierto'},
        ),
    ]