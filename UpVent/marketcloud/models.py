from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Product(models.Model):

    STATUS = (
        (0, "Oculto"),
        (1, "Publicado")
    )

    icon = models.ImageField(
        verbose_name="Ícono del producto"
    )

    name = models.CharField(
        verbose_name="Nombre del Producto",
        max_length=50,
        unique=True,
        help_text="Ingrese el nombre del producto",
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

    price = models.DecimalField(
        verbose_name="Precio del Producto",
        max_digits=5,
        decimal_places=2,
        help_text="Ingrese el precio del producto. Es recomendable usar solo\
        dos decimales en caso de necesitar el uso de los mismos."
    )

    category = models.CharField(
        verbose_name="Categoría del producto",
        max_length=50,
        help_text="Ingrese la categoría a la que pertenece el producto.\
        e.g: Herramientas de Desarrollador, Frameworks, Blogs y Foros.",
        default="",
        blank=False
    )

    apptype = models.CharField(
        verbose_name="Tipo de aplicación",
        max_length=50,
        help_text="Ingrese el tipo de aplicación que es el producto.\
        e.g: Suscripción, App de 1 click, etc.",
        default="",
        blank=False
    )

    short_description = models.TextField(
        verbose_name="Descripción corta del producto",
        help_text="Ingrese una descripción corta del producto.",
        default="",
        blank=False
    )

    description = RichTextUploadingField(
        verbose_name="Descripción detallada del producto",
        help_text="Ingrese una descripción detallada del producto."
    )

    created_on = models.DateTimeField(
        verbose_name="Creado el: ",
        auto_now_add=True
    )

    # Blog publishing status
    status = models.IntegerField(
        choices=STATUS,
        default=0,
        help_text="Estatus actual del producto"
    )

    class Meta:
        ordering = ['created_on']
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.title
