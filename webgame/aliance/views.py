from django.shortcuts import render
from .forms import Upload

def index(request):
    return render(request, 'aliance/index.html')

def upload(request):
    form = Upload()
    return render(request, 'aliance/upload.html', {
        'upload_file': form 
        })
