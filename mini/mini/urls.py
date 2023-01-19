from django.contrib import admin
from django.urls import path, include

from urlShortener.views.redirectUrlView import RedirectUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('mini/', include('urlShortener.urls')),
    path('', include('mini.swaggerUrls')),
    path('<str:slug>/', RedirectUrl.as_view(), name='urlredirect'),
]
