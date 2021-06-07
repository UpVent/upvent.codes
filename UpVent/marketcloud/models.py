from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Product(models.Model):

    STATUS = (
        (0, "Agotado"),
        (1, "Disponible")
    )

    icon = models.ImageField(
        verbose_name="Ícono del producto",
        upload_to="store"
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

    # This is expressed in cents
    price = models.DecimalField(
        verbose_name="Precio del Producto",
        decimal_places=2,
        max_digits=8,
        help_text="Ingrese el precio del producto. Es recomendable usar solo\
        dos decimales en caso de necesitar el uso de los mismos.",
        default=0
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

    stripe_link = models.URLField(
        verbose_name="Enlace para pagos con cripto en Stripe",
        help_text="Ingrese el enlace para pagos con stipe",
        blank=True
    )

    created_on = models.DateTimeField(
        verbose_name="Creado el: ",
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        verbose_name="Actualizado el: ",
        auto_now_add=True
    )

    # Product inventory status
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
        return self.name

class TOS(models.Model):

    """
    Stores a single and UNIQUE terms of service + refund policy to make this
    site compliant with inside / outside country trade laws.

    This model has an overriden save() method to prevent more than one privacy
    policy instance to be created.
    """

    title = models.CharField(
        verbose_name="Título",
        max_length=100,
        help_text="Ingrese el título para sus términos y condiciones",
        default="Términos y Condiciones + Política de Reembolsos",
        blank=False
    )

    created_on = models.DateField(
        verbose_name="Fecha de Creación",
        auto_now_add=True
    )

    updated_on = models.DateField(
        verbose_name="Fecha de Actualización",
        auto_now_add=True
    )

    changelog = models.TextField(
        verbose_name="Registro de Cambios",
        help_text="Ingrese la razón de cambiar este documento.",
        blank=False
    )

    text = RichTextUploadingField(
        verbose_name="Términos del servicio",
        help_text="Escriba aquí su política de reembolsos y términos"
    )

    class Meta:
        verbose_name = "Términos del servicio"
        verbose_name_plural = "Términos del servicio"

    def __str__(self):
        return self.title

    # Override 'save' method to allow only ONE instance for TOS
    def save(self, *args, **kwargs):
        if not self.pk and TOS.objects.exists():
            raise TOS('You cannot have more than one tos entry')
        return super(TOS, self).save(*args, **kwargs)
