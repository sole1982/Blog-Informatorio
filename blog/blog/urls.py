from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from .views import index
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.usuario.views import RegistrarUsuario, LoginUsuario, LogoutUsuario 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('apps.posts.urls')),
    path('', include('apps.contacto.urls')),
    path('registrar/', RegistrarUsuario.as_view(), name='registrar'),  
    path('login/', LoginUsuario.as_view(), name='login'),  
    path('logout/', LogoutUsuario.as_view(), name='logout'),  
    

]  +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
