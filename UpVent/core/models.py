from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# (about-us) Project model
class Project(models.Model):

    title = models.CharField(
        verbose_name="Título",
        max_length=200,
        unique=True
    )

    image = models.ImageField(
        verbose_name="Imágen Destacada",
        upload_to="portfolio"
    )

    site = models.URLField(
        verbose_name="Sitio web",
        max_length=200,
    )

    description = RichTextUploadingField(
        verbose_name="Descripción"
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
