from django.contrib import admin

from .models import Rifa, Premio, Compra, Numero

# Register your models here.
class RifaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_rifa', 
        'descripcion_rifa', 
        'fecha_inicio_rifa',
        'fecha_termino_rifa',
        'cantidad_numeros_rifa',
        'estado_rifa',
        ]
    
class PremioAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_premio', 
        'descripcion_premio', 
        'imagen_premio',
        'comprador',
        'rifa',
        ]
    list_display_links = ['nombre_premio', 'rifa']
    search_fields = ['nombre_premio', 'rifa__nombre_rifa']

    
class CompraAdmin(admin.ModelAdmin):
    list_display = [
        'nombre_cliente', 
        'email_cliente', 
        'telefono_cliente',
        'rifa',
        ]

class NumeroAdmin(admin.ModelAdmin):
    list_display = [
        'numero', 
        'codigo_pago',
        'estado_pago',
        'comprador',
        'rifa'
        ]

admin.site.register(Rifa, RifaAdmin)
admin.site.register(Premio, PremioAdmin)
admin.site.register(Compra, CompraAdmin)
admin.site.register(Numero, NumeroAdmin)