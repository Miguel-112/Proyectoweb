from django.urls import path

from ProyectoWebApp import views

from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    
    path('',views.home, name="Home"),
   
   
   
   

]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #aqui le dammos le decimos donde estan las imagenes para que se puedan ver en el panel de administracion