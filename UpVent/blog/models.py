from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Current blog post status
STATUS = (
    (0, "Draft"),
    (1, "Published")
)

class Post(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200, unique=True)
    image = models.ImageField(verbose_name="Imágen Destacada", upload_to="posts")
    category = models.CharField(verbose_name="Categoría", max_length=20, default='None')
    slug = models.SlugField(verbose_name="Slug", max_length=200, unique=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(verbose_name="Actualizado el: ", auto_now= True)
    content = RichTextUploadingField(verbose_name="Contenido")
    created_on = models.DateTimeField(verbose_name="Creado el: ", auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
