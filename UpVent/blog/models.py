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
        unique=True)

    # Blog portrait
    image = models.ImageField(
        verbose_name="Imágen Destacada",
        upload_to="posts",
        blank=True
    )

    # Blog category
    category = models.CharField(
        verbose_name="Categoría",
        max_length=20,
        default='None'
    )

    # Blog slug (autogenerated)
    slug = models.SlugField(
        verbose_name="Slug",
        max_length=200,
        unique=True
    )

    # Blog author (get from current user)
    author = models.ForeignKey(
        User,
        verbose_name="Autor",
        on_delete= models.CASCADE,related_name='blog_posts'
    )

    # Blog last update date
    updated_on = models.DateTimeField(
        verbose_name="Actualizado el: ",
        auto_now= True
    )

    # Blog content (Handled by CKEditor)
    content = RichTextUploadingField(
        verbose_name="Contenido"
    )

    # Blog creation date
    created_on = models.DateTimeField(
        verbose_name="Creado el: ",
        auto_now_add=True
    )

    # Blog publishing status
    status = models.IntegerField(
        choices=STATUS,
        default=0
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):

    # Which model is related to which post
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE
    )

    # Name or nickname of the commenter
    name = models.CharField(verbose_name="Nombre", max_length=255)

    # The email of the commenter (Used to prevent spam)
    email = models.EmailField(verbose_name="Email", default="mail@mail.com")

    # The website of the commenter (Optional)
    website = models.CharField(verbose_name="Sitio Web", blank=True, default='', max_length=255)

    # The comment body
    body = models.TextField(verbose_name="Comentario")

    # The date the comment was made
    date_added = models.DateTimeField(verbose_name="Fecha de publicación", auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
