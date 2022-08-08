from django.contrib import admin

# Register your models here.


from .models import Pedido,LineaPedidos

# Register your models here.






admin.site.register([Pedido,LineaPedidos])
