from django.shortcuts import render

# Create your views here.

def index(request):
     """ VISTAS para el catalogo de prodcutos """

     return render(request, 'index.html')