from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Product(models.Model):

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
