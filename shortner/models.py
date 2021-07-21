from django.db import models
from django.conf import settings

# Create your models here.
class url(models.Model):
    url = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'{settings.ALLOWED_HOSTS[0]}/{self.uuid}' 