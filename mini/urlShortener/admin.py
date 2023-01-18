from django.contrib import admin

# Register your models here.
# from urlShortener.models import urlmodel
from .models.urlmodel import UrlData

admin.site.register((UrlData))
