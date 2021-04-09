from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# (about-us) Project model
class Project(models.Model):

    title = models.CharField(
        verbose_name="Título",
        max_length=200,
        unique=True,
        help_text="Ingrese el nombre del proyecto"
    )

    image = models.ImageField(
        verbose_name="Imágen Destacada",
        upload_to="portfolio",
        help_text="Se recomiendan imágenes de dimensiones rectangulares. Solo formatos jpg, jpeg, png y webm"
    )

    site = models.URLField(
        verbose_name="Sitio web",
        max_length=200,
        help_text="El sitio web donde se encuentra alojado el proyecto"
    )

    description = RichTextUploadingField(
        verbose_name="Descripción",
        help_text="Descripción del proyecto. Procure ser breve."
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['created_on']
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.title
