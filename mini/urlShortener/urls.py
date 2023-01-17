from django.urls import path

from .views.shortenUrlView import ShortenUrl
app_name = 'accounts'


urlpatterns = [

    path('long/', ShortenUrl.as_view(), name='shortenurl'),
]