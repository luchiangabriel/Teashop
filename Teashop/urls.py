
"""Teashop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic import RedirectView
from Teashop.views import homepage_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', homepage_view),
    path('polls/', include('polls.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('distributors/', include('distributors.urls')),
    path('ingredients/', include('ingredients.urls')),
    path('recipes/', include('recipes.urls')),
    path(
        "favicon.ico/",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    )
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)