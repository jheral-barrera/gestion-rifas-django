from django.db import models

# Create your models here.
class Rifa(models.Model):
    ESTADOS = [
        ('oculta', 'Oculta'),
        ('disponible', 'Disponible'),
        ('finalizada', 'Finalizada'),
        ('anulada', 'Anulada')
    ]

    nombre_rifa = models.CharField(max_length=100)
    descripcion_rifa =  models.TextField()
    fecha_inicio_rifa = models.DateField()
    fecha_termino_rifa = models.DateField()
    cantidad_numeros_rifa = models.PositiveIntegerField()
    estado_rifa = models.CharField(max_length=10, choices=ESTADOS, default='disponible')

    def __str__(self):
        return self.nombre_rifa

class Compra(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField(max_length=254, null=True, blank=True)
    telefono_cliente = models.PositiveIntegerField()
    rifa = models.ForeignKey(Rifa, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre_cliente} - Rifa: {self.rifa.nombre_rifa}'

class Premio(models.Model):
    nombre_premio = models.CharField(max_length=100)    
    descripcion_premio = models.TextField()
    imagen_premio = models.ImageField(upload_to='premios', null=True, blank=True)
    comprador = models.ForeignKey(Compra,  on_delete=models.CASCADE, null=True, blank=True)
    rifa = models.ForeignKey(Rifa, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre_premio} - Rifa: {self.rifa.nombre_rifa}'

class Numero(models.Model):
    numero = models.PositiveIntegerField()
    codigo_pago = models.CharField(max_length=50, null=True, blank=True)
    estado_pago = models.CharField(max_length=10, null=True, blank=True)
    comprador = models.ForeignKey(Compra, on_delete=models.CASCADE)
    rifa = models.ForeignKey(Rifa, on_delete=models.CASCADE)

    def __str__(self):
        return f'Número {self.numero} - Compra: {self.comprador}'