from django.db import models


# (about-us) Project model
class Project(models.Model):

    # Project tile
    title = models.CharField(
        verbose_name='Título',
        max_length=200,
        unique=True
    )

    # Project image
    image = models.ImageField(
        verbose_name='Imágen Destacada',
        upload_to='portfolio'
    )
