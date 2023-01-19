from django.db import models


# Model for the project
class UrlData(models.Model):
    name = models.CharField(max_length=300, blank=False, null=True, unique=True)
    long_url = models.CharField(max_length=300, blank=False, null=False, unique=True)
    short_url = models.CharField(max_length=20, blank=False, null=False, unique=True)
    slug = models.CharField(max_length=8, unique=True)
    no_of_uses = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return self.name
