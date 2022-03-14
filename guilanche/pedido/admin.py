from django.contrib import admin
from .models import Pedido
from .forms import PedidoForm

# Register your models here.
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['lanche']
    form = PedidoForm
admin.site.register(Pedido)