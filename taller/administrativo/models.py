from django.db import models

# Create your models here.
class Edificio(models.Model):
    opciones_edificio = (
        ('residencial', 'residencial'), 
        ('comercial', 'comercial')
    )

    nombre = models.CharField(max_length=80)
    direccion = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=50)
    tipo = models.CharField(choices=opciones_edificio, max_length=15)

    def __str__(self):
        return "%s %s %s %s" % (self.nombre,
                self.direccion,
                self.ciudad,
                self.tipo
            )

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    costo_dept = models.IntegerField('Costo del departamento')
    num_dept = models.IntegerField('Número de departamentos')
    num_cuarto = models.IntegerField('Número de Cuartos')
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE,
            related_name="ubicacion")

    def __str__(self):
        return "%s %s %s %s %s" % (self.nombre, 
                self.costo_dept,
                self.num_dept,
                self.num_cuarto,
                self.edificio
            )