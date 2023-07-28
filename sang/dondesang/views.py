from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    pays = Pays.objects.all()
    region=Region.objects.all()
    ville=Ville.objects.all()
    context={
        'pays':pays,
        'region':region,
        'ville':ville,
    }
    return render(request, 'index.html',context)
