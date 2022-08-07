from django.shortcuts import render,redirect

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.


class VRegistro(View):

    def get(self, request):
        form=UserCreationForm()
        return render(request, "registro/registro.html", {"form":form})
        csrf_protect()

    def post(self,request):
        

        form=UserCreationForm(request.POST)

        if form.is_valid():


            usuario=form.save()

            login(request, usuario)

            return redirect('Home')
            csrf_protect()

        else:
              # pass se usa para probar codigo
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "registro/registro.html", {"form":form})
            csrf_protect()


def  cerrar_sesion(request):

    logout(request)
    return redirect('Home')
    csrf_protect()

def logear(request):

    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            NOMBRE_USUARIO=form.cleaned_data.get("username")
            CONTRASENIA=form.cleaned_data.get("password")

            usuario=authenticate(username=NOMBRE_USUARIO,password=CONTRASENIA)
            
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
                csrf_protect()
            else:
                messages.error(request, 'usuario no valido')
        else:
              messages.error(request, 'informacion incorrecta')


    form=AuthenticationForm
    return render(request, "login/login.html", {"form":form})
    csrf_protect()

