"""
URL configuration for TuPrimerPaginaCaminos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.clinica, name='clinica')
Class-based views
    1. Add an import:  from other_app.views import Clinica
    2. Add a URL to urlpatterns:  path('', Clinica.as_view(), name='clinica')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinica.urls')),
]
