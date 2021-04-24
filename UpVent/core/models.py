from django.db import models
from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField

# (about-us) Project model
class Project(models.Model):

    """
    Stores a single instance of a project used in the portfolio section
    in this site.
    """

    title = models.CharField(
        verbose_name="Título",
        max_length=200,
        unique=True,
        help_text="Ingrese el nombre del proyecto."
    )

    image = models.ImageField(
        verbose_name="Imágen Destacada",
        upload_to="portfolio",
        help_text="Se recomiendan imágenes de dimensiones rectangulares."
    )

    site = models.URLField(
        verbose_name="Sitio web",
        max_length=200,
        help_text="El sitio web donde se encuentra alojado el proyecto."
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

# (services) Free Software Services Model
class FSProject(models.Model):

    """
    Stores a single Free Software Project shown in the "services" page of this
    site.
    """

    title = models.CharField(
        verbose_name="Título",
        max_length=100,
        help_text="Ingrese el nombre del proyecto.",
        default=""
    )

    image = models.ImageField(
        verbose_name="Imágen Destacada",
        upload_to="floss",
        help_text="Se recomiendan imágenes de dimensiones rectangulares."
    )

    description = RichTextUploadingField(
        verbose_name="Descripción",
        help_text="Descripción del proyecto."
    )


    github_addr = models.URLField(
        verbose_name="Dirección de Git",
        max_length=200,
        help_text="URL completa del repositorio donde se encuentra el proyecto",
        default="https://github.com/"
    )

    support_addr = models.URLField(
        verbose_name="Dirección de apoyo",
        max_length=200,
        help_text="URL completa donde los visitantes podrán apoyar al proyecto",
        default="https://github.com/"
    )

    plicense = models.CharField(
        verbose_name="Licencia",
        max_length=25,
        help_text="Ingrese la licencia del proyecto",
        default=""
    )

    license_link = models.URLField(
        verbose_name="URL de licencia",
        max_length=200,
        help_text="URL completa para ver la licencia del proyecto",
        default="https://gnu.org/"
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Proyecto de código abierto"
        verbose_name_plural = "Proyectos de código abierto"

    def __str__(self):
        return self.title

# (licenses) License Model
class License(models.Model):

    """
    Stores a single License model shown in the "licenses" page of this
    site.
    """

    name = models.CharField(
        verbose_name="Nombre",
        max_length=60,
        help_text="Ingrese el nombre de la licencia a mostrar",
        default="Gnu General Public License v2"
    )

    verbatim = RichTextUploadingField(
        verbose_name="Texto corto de la licencia",
        help_text="Escriba aquí el texto corto o resumen de la licencia",
        default=""
    )

    license_link = models.URLField(
        verbose_name="URL de licencia",
        max_length=200,
        help_text="URL completa para ver la licencia del proyecto",
        default="https://gnu.org/"
    )

    class Meta:
        verbose_name = "Licencia"
        verbose_name_plural = "Licencias"

    def __str__(self):
        return self.name

# (licenses) HOF Model
class HOF(models.Model):

    """
    Stores a single Hall Of Fame Project shown in the "licenses" page of this
    site.
    """

    name = models.CharField(
        verbose_name="Nombre",
        max_length=60,
        help_text="Ingrese el nombre del proyecto a mostrar en\
        el salón de la fama",
        default="Gnu Compiler Colection"
    )

    icon = models.ImageField(
        verbose_name="Icono del Proyecto",
        upload_to="licenses",
        help_text="Se recomiendan imágenes de dimensiones rectangulares."
    )

    class Meta:
        verbose_name = "Proyecto del salón de la fama"
        verbose_name_plural = "Proyectos del salón de la Fama"

    def __str__(self):
        return self.name

# (privacy-policy) Privacy Policy Project Model
class PrivacyPolicy(models.Model):

    """
    Stores a single and UNIQUE privacy policy to make this site compliant with
    inside / outside country privacy laws.

    This model has an overriden save() method to prevent more than one privacy
    policy instance to be created.
    """

    title = models.CharField(
        verbose_name="Título",
        max_length=100,
        help_text="Ingrese el título para su política de privacidad",
        default="Política de Privacidad"
    )

    created_on = models.DateField(
        auto_now_add=True
    )

    updated_on = models.DateField(
        auto_now_add=True
    )

    changelog = models.TextField(
        verbose_name="Registro de Cambios",
        help_text="Ingrese la razón de cambiar la política de privacidad."
    )

    text = RichTextUploadingField(
        verbose_name="Política de privacidad",
        help_text="Escriba aquí su política de privacidad"
    )

    class Meta:
        verbose_name = "Política de Privacidad"
        verbose_name_plural = "Política de Privacidad"

    def __str__(self):
        return self.title

    # Override 'save' method to allow only ONE instance for privacy policy
    def save(self, *args, **kwargs):
        if not self.pk and PrivacyPolicy.objects.exists():
            raise ValidationError('You cannot have more than one privacy policy')
        return super(PrivacyPolicy, self).save(*args, **kwargs)
