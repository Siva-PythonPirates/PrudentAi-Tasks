from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import UploadedImage
from PIL import Image
import os
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

@api_view(['POST'])
def upload_image(request):
    file = request.FILES.get('image')
    if not file:
        return JsonResponse({'error': 'No image uploaded'}, status=400)
    
    uploaded_image = UploadedImage.objects.create(image=file)
    return JsonResponse({'id': uploaded_image.id})

@api_view(['GET'])
def get_resized_images(request, id):
    image_entry = get_object_or_404(UploadedImage, id=id)
    image_path = image_entry.image.path

    base, ext = os.path.splitext(image_entry.image.name)
    small_path = f'{base}_small{ext}'
    medium_path = f'{base}_medium{ext}'

    small_url = request.build_absolute_uri(f'/media/{small_path}')
    medium_url = request.build_absolute_uri(f'/media/{medium_path}')
    original_url = request.build_absolute_uri(image_entry.image.url)

    if not os.path.exists(os.path.join(image_entry.image.storage.location, small_path)):
        with Image.open(image_path) as img:
            img_small = img.resize((int(img.width * 100 / img.height), 100))
            img_small.save(os.path.join(image_entry.image.storage.location, small_path))

            img_medium = img.resize((int(img.width * 300 / img.height), 300))
            img_medium.save(os.path.join(image_entry.image.storage.location, medium_path))

    return JsonResponse({
        'small': small_url,
        'medium': medium_url,
        'original': original_url,
    })
