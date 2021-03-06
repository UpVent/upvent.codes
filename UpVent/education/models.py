from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Resource(models.Model):
    """
    Stores a single 'Book' model shown in the 'education' url of this site
    """

    Libro = "Libro"
    Video = "Vídeo"
    Otro = "Otro"

    CATEGORIES = (
        (Libro, "Libro"),
        (Video, "Vídeo"),
        (Otro, "Otro"),
    )

    title = models.CharField(
        verbose_name="Nombre",
        max_length=100,
        help_text="Ingrese el título del libro",
        default="",
        blank=False
    )

    slug = models.SlugField(
        verbose_name="Slug",
        max_length=200,
        unique=True,
        help_text="Campo autogenerado. Modifique de acuerdo a sus necesidades",
        blank=False
    )

    category = models.CharField(
        verbose_name="Categoría",
        choices = CATEGORIES,
        max_length=7,
        help_text="Ingrese a que categoría pertenece el recurso",
        default=Libro,
        blank=False
    )

    image = models.ImageField(
        verbose_name="Imágen Destacada",
        upload_to="education",
        help_text="Se recomiendan imágenes de dimensiones coherentes.",
        blank=False
    )

    description = RichTextUploadingField(
        verbose_name="Descripción",
        help_text="Descripción del proyecto."
    )

    donate_link = models.URLField(
        verbose_name="Enlace del botón de donar",
        max_length=200,
        help_text="Ingrese el enlace a donde donarán los consultantes",
        default="",
        blank=True
    )

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"

    def __str__(self):
        return self.title
