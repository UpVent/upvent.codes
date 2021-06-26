from django.db import models

class Book(models.Model):
    """
    Stores a single 'Book' model shown in the 'education' url of this site
    """

    title = models.CharField(
        verbose_name="Nombre",
        max_length=100,

    )
