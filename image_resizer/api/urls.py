from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Serve the homepage
    path('image/', views.upload_image, name='upload_image'),
    path('image/<int:id>/', views.get_resized_images, name='get_resized_images'),
]
