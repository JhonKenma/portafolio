from django.contrib import admin
from django.urls import path, include  # Para incluir los urls de blog
from django.conf import settings
from django.conf.urls.static import static
# AGREGADOS AQUI
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta del admin
    path('', views.about, name='about'),  # Ruta para la página de inicio (principal)
    path('projects/', views.projects, name='projects'),  # Ruta para la sección sobre mí
    # Ruta para la sección de proyectos
    path('skills/', views.skills, name='skills'),  # Ruta para la sección de habilidades
    path('contact/', views.contact, name='contact'),  # Ruta para la sección de contacto
]

# Si estás en modo DEBUG, configura las rutas para los archivos estáticos
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
