from django.shortcuts import render
from .forms import DressGenerationForm
from .utils import generate_dress
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os
def index(request):
    return render(request, 'generator/index.html')  # Make sure 'index.html' exists


# def generate_dress_view(request):
#     if request.method == 'POST':
#         form = DressGenerationForm(request.POST)
#         if form.is_valid():
#             prompt = form.cleaned_data['prompt']
#             # Generate the dress image
#             image_buffer = generate_dress(prompt)
            
#             if image_buffer:
#                 # Return the image as an HTTP response
#                 response = HttpResponse(image_buffer, content_type="image/png")
#                 response['Content-Disposition'] = 'inline; filename="generated_dress.png"'
#                 return response
#             else:
#                 error_message = "An error occurred while generating the dress. Please try again."
#                 return render(request, 'generator/generate_dress.html', {'form': form, 'error_message': error_message})
#     else:
#         form = DressGenerationForm()

#     return render(request, 'generator/generate_dress.html', {'form': form})
def generate_dress_view(request):
    generated_image_url = None  # Default image URL
    error_message = None

    if request.method == 'POST':
        form = DressGenerationForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']

            # Generate the dress image using the utility function
            image_buffer = generate_dress(prompt)
            if image_buffer:
                # Save the image to MEDIA_ROOT
                output_path = os.path.join(settings.MEDIA_ROOT, 'generated_dress.png')
                with open(output_path, 'wb') as f:
                    f.write(image_buffer.read())

                # Create the URL to serve the image
                generated_image_url = os.path.join(settings.MEDIA_URL, 'generated_dress.png')
            else:
                error_message = "An error occurred while generating the dress. Please try again."
    else:
        form = DressGenerationForm()

    return render(request, 'generator/generate_dress.html', {
        'form': form,
        'generated_image_url': generated_image_url,
        'error_message': error_message,
    })
