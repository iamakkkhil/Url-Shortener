from django.db import models

# Create your models here.
class url(models.Model):
    url = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10, unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'URL : /{self.uuid}' 