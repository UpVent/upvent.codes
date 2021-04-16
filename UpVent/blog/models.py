from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Current blog post status
STATUS = (
    (0, "Draft"),
    (1, "Published")
)

class Post(models.Model):
    # Blog Title
    title = models.CharField(
        verbose_name="Título",
        max_length=200,
        unique=True,
        help_text="Título del post"
    )

    # Blog portrait
    image = models.ImageField(
        verbose_name="Imágen Destacada",
        upload_to="posts",
        help_text="Portada del post. Se recomiendan imágenes rectangulares."
    )

    # Blog category
    category = models.CharField(
        verbose_name="Categoría",
        max_length=20,
        default='None',
        help_text="Categoría a la que pertenece el post."
    )

    # Blog slug (autogenerated)
    slug = models.SlugField(
        verbose_name="Slug",
        max_length=200,
        unique=True,
        help_text="Campo autogenerado, no tocar"
    )

    # Blog author (get from current user)
    author = models.ForeignKey(
        User,
        verbose_name="Autor",
        on_delete= models.CASCADE,related_name='blog_posts',
        help_text="Seleccione el autor del post"
    )

    # Blog last update date
    updated_on = models.DateTimeField(
        verbose_name="Actualizado el: ",
        auto_now= True
    )

    # Blog content (Handled by CKEditor)
    content = RichTextUploadingField(
        verbose_name="Contenido",
        help_text="Contenido detallado del post"
    )

    # Blog creation date
    created_on = models.DateTimeField(
        verbose_name="Creado el: ",
        auto_now_add=True
    )

    # Blog publishing status
    status = models.IntegerField(
        choices=STATUS,
        default=0,
        help_text="Estatus actual del post"
    )

# ----- Blog side panel attributes -----

    # Blog side title
    side_title = models.CharField(
        verbose_name="Título Lateral",
        max_length=200,
        help_text="Título de la imágen que aparecerá en la parte derecha de\
        cada post"
    )

    # Blog Side image
    side_img = models.ImageField(
        verbose_name="Imágen Lateral",
        upload_to="posts",
        help_text="Imágen que aparecera en la parte derecha de cada post.\
        puede usarse para publicidad u otros fines."
    )

    # Blog side text
    site_text = models.TextField(
        verbose_name="Texto Lateral",
        help_text="Texto mostrado en la parte derecha de cada post, debajo de\
        la imágen lateral."
    )

    # Blog side button
    side_button = models.CharField(
        verbose_name="Texto del botón lateral",
        max_length=50,
        default="Leer más...",
        help_text="Texto que mostrará el botón mostrado en la parte derecha\
        de cada post."
    )

    # Blog side button url
    side_button_url = models.URLField(
        verbose_name="URL del botón lateral",
        help_text="Sitio al que dirigirá el botón lateral mostrado en la parte\
        derecha de cada post"
    )

    side_video_title = models.CharField(
        verbose_name="Texto del vídeo lateral",
        max_length=100,
        default="Conocer más",
        help_text="Texto que se mostrará como título del vídeo lateral"
    )

    # Blog side video
    side_video = models.URLField(
        verbose_name="Video Lateral",
        help_text="URL hacia un vídeo que será mostrado en la parte derecha de\
        cada post."
    )

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title

class Comment(models.Model):

    # Which model is related to which post
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE,
        help_text="A que post pertenece este comentario"
    )

    # Name or nickname of the commenter
    name = models.CharField(
        verbose_name="Nombre",
        max_length=255,
        help_text="Nombre de la persona que realizó el comentario"
    )

    # The email of the commenter (Used to prevent spam)
    email = models.EmailField(
        verbose_name="Email",
        default="mail@mail.com",
        help_text="Correo electrónico de la persona que realizó el comentario"
    )

    # The website of the commenter (Optional)
    website = models.CharField(
        verbose_name="Sitio Web",
        blank=True,
        default='',
        max_length=255,
        help_text="Sitio web de la persona que realizó el comentario"
    )

    # The comment body
    body = models.TextField(
        verbose_name="Comentario",
        help_text="Cuerpo del comentario"
    )

    # The date the comment was made
    date_added = models.DateTimeField(
        verbose_name="Fecha de publicación",
        auto_now_add=True
    )

    class Meta:
        ordering = ['date_added']
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
