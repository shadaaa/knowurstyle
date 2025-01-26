from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generate-dress/', views.generate_dress_view, name='generate_dress'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
