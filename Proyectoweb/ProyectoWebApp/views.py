from django.shortcuts import render,HttpResponse

from servicios.models import Servicios

# Create your views here.



def home(request):

    return render(request,"ProyectoWebApp/home.html")






def tienda(request):

     return render(request,"ProyectoWebApp/tienda.html")






