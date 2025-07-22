from django.shortcuts import render
from .forms import Upload
from . import models
from bs4 import BeautifulSoup
import io

def index(request):
    return render(request, 'aliance/index.html')

def upload(request):
    form = Upload()
    return render(request, 'aliance/upload.html', {
        'upload_file': form 
        })
