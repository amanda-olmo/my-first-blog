from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # una relacion (link) con otro modelo.
    title = models.CharField(max_length=200)  # texto con un numero limitado de caracteres.
    text = models.TextField()  # texto largo sin limite de caracteres. 
    created_date = models.DateTimeField(
            default=timezone.now)  # fecha y hora
    published_date = models.DateTimeField(
            blank=True, null=True)  # fecha y hora

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title