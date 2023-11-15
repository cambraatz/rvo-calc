from django.shortcuts import render
import re
from django.utils.timezone import datetime
from django.http import HttpResponse

def home(request):
    return render(request, "portfolio/home.html")

def about(request):
    return render(request, "portfolio/about.html")

def contact(request):
    return render(request, "portfolio/contact.html")

def hello_there(request,name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'portfolio/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )