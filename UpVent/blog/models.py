from django.db import models
from django.contrib.auth.models import User

# Current blog post status
STATUS = (
    (0, "Draft"),
    (1, "Published")
)

class Post(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200, unique=True)
    category = models.CharField(verbose_name="Categoría", max_length=20)
    slug = models.SlugField(verbose_name="Slug", max_length=200, unique=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(verbose_name="Actualizado el: ", auto_now= True)
    content = models.TextField(verbose_name="Contenido")
    created_on = models.DateTimeField(verbose_name="Creado el: ", auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
