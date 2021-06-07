from django.db import models
from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField

# (index) Testimonial Model
class Testimonial(models.Model):

    """
    Stores a single instance of a testimonial made by any UpVent client.
    """

    image = models.ImageField(
        verbose_name="Foto del cliente",
        upload_to="testimonials",
        help_text="Se recomiendan imágenes cuadradas",
        blank=False
    )

    name = models.CharField(
        verbose_name="Nombre Completo",
        max_length=100,
        unique=True,
        help_text="Ingrese el nombre de la persona dando su testimonio.",
        default="",
        blank=False
    )

    testimonial = RichTextUploadingField(
        verbose_name="Testimonio",
        help_text="Testimonio de la persona."
    )

    workplace = models.CharField(
        verbose_name="Lugar de Trabajo",
        max_length=80,
        help_text="Ingrese el puesto que desempeña la persona que da el\
        testimonio.",
        blank=False
    )

    site = models.URLField(
        verbose_name="Sitio web",
        max_length=200,
        help_text="El sitio web donde se encuentra alojado el proyecto.",
        blank=False
    )

    class Meta:
        verbose_name = "Testimonio"
        verbose_name_plural = "Testimonios"

    def __str__(self):
        return self.name

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
        help_text="Ingrese el nombre del proyecto.",
        blank=False
    )

    image = models.ImageField(
        verbose_name="Imágen Destacada",
        upload_to="portfolio",
        help_text="Se recomiendan imágenes de dimensiones rectangulares.",
        blank=False
    )

    site = models.URLField(
        verbose_name="Sitio web",
        max_length=200,
        help_text="El sitio web donde se encuentra alojado el proyecto.",
        blank=False
    )

    description = RichTextUploadingField(
        verbose_name="Descripción",
        help_text="Descripción del proyecto. Procure ser breve."
    )

    created_on = models.DateTimeField(
        verbose_name="Fecha de Creación",
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        verbose_name="Fecha de Actualización",
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
        default="",
        blank=False
    )

    image = models.ImageField(
        verbose_name="Imágen Destacada",
        upload_to="floss",
        help_text="Se recomiendan imágenes de dimensiones rectangulares.",
        blank=False
    )

    description = RichTextUploadingField(
        verbose_name="Descripción",
        help_text="Descripción del proyecto."
    )


    github_addr = models.URLField(
        verbose_name="Dirección de Git",
        max_length=200,
        help_text="URL completa del repositorio donde se encuentra el proyecto",
        default="https://github.com/",
        blank=False
    )

    support_addr = models.URLField(
        verbose_name="Dirección de apoyo",
        max_length=200,
        help_text="URL completa donde los visitantes podrán apoyar al proyecto",
        default="https://github.com/",
        blank=False
    )

    plicense = models.CharField(
        verbose_name="Licencia",
        max_length=25,
        help_text="Ingrese la licencia del proyecto",
        default="",
        blank=False
    )

    license_link = models.URLField(
        verbose_name="URL de licencia",
        max_length=200,
        help_text="URL completa para ver la licencia del proyecto",
        default="https://gnu.org/",
        blank=False
    )

    created_on = models.DateTimeField(
        verbose_name="Fecha de Creación",
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        verbose_name="Fecha de Actualización",
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
        default="Gnu General Public License v2",
        blank=False
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
        default="https://gnu.org/",
        blank=False
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
        default="Gnu Compiler Colection",
        blank=False
    )

    icon = models.ImageField(
        verbose_name="Icono del Proyecto",
        upload_to="licenses",
        help_text="Se recomiendan imágenes de dimensiones rectangulares.",
        blank=False
    )

    class Meta:
        verbose_name = "Proyecto del salón de la fama"
        verbose_name_plural = "Proyectos del salón de la Fama"

    def __str__(self):
        return self.name

# (team) Team member Model
class TeamMember(models.Model):
    """
    Stores a single team member to show on the 'team/' url in this page.

    The is_collab field is a boolean to indicate if the team member is an
    outside collaborator. The status is pretty simple.

    True = Is an outside collaborator
    False = Is a staff member
    """

    image = models.ImageField(
        verbose_name="Foto del integrante",
        upload_to="team",
        help_text="Se recomiendan imágenes de dimensiones rectangulares.",
        blank=False
    )

    name = models.CharField(
        verbose_name="Nombre del Integrante del equipo",
        max_length=100,
        help_text="Ingrese el nombre del integrante del equipo",
        default="",
        blank=False
    )

    position = models.CharField(
        verbose_name="Posición o contribución",
        max_length=100,
        help_text="Ingrese en que ha contribuido o que posición dentro\
        de UpVent tiene el integrante.",
        default="",
        blank=False
    )

    is_collab = models.BooleanField(
        verbose_name="¿Es un colaborador externo?",
        help_text="Indicar si el miembro siendo registrado es un colaborador\
        externo, de no serlo se tomará como miembro de UpVent",
        default=False,
        null=False
    )

    class Meta:
        verbose_name = "Miembro del equipo"
        verbose_name_plural = "Miembros del equipo"

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
        default="Política de Privacidad",
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
        help_text="Ingrese la razón de cambiar la política de privacidad.",
        blank=False
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

# Terms Of Service Model
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
