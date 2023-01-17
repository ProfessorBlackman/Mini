from django.db import models


# Create your models here.
class UrlData(models.Model):
    long_url = models.CharField(max_length=300)
    short_url = models.CharField(max_length=20)
    slug = models.CharField(max_length=10)
    no_of_uses = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
