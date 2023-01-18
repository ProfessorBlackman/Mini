from django.urls import path

from .views.shortenUrlView import ShortenUrl
app_name = 'urlShortener'


urlpatterns = [

    path('long/', ShortenUrl.as_view(), name='shortenurl'),
]