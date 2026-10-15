from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet

router = DefaultRouter()
router.register(r'articulos', ArticuloViewSet, basename='api-articulo')

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('articulos', views.articulos, name='articulos'),
    path('articulos/crear', views.crear, name='crear'),
    path('articulos/editar/<int:id>', views.editar, name='editar'),
    path('articulos/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)