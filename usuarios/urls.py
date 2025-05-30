"""from django.urls import path
from usuarios.views import login, registro, editar_perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('login/', login, name="login"),
   path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),
   path('registro/', registro, name="registro"),
   path('perfil/editar/', editar_perfil, name="editar_perfil"),
]"""

from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import login, registro, editar_perfil

urlpatterns = [
   path('login/', login, name="login"),
   path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name="logout"),
   path('registro/', registro, name="registro"),
   path('perfil/editar/', editar_perfil, name="editar_perfil"),
   path('', include('clinica.urls')),  # Incluye las URLs de la app clinica
]

# Configuración para servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
