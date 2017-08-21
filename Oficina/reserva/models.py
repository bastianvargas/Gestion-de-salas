from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import format_html


from django.db import models

@python_2_unicode_compatible
class Usuario(models.Model):
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	cargo = models.CharField(max_length=50)
	user = models.CharField(max_length=20)
	passw = models.CharField(max_length=20)
	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Insumo(models.Model):
	nombre = models.CharField(max_length=200)
	cantidad = models.IntegerField(default=1)
	def __str__(self):
		return self.nombre

@python_2_unicode_compatible
class Sala(models.Model):
	nombre = models.CharField(max_length=60)
	capacidad = models.IntegerField(default=0)
	ubicacion = models.CharField(max_length=200)
	horario_disponible = models.DateTimeField(auto_now_add=True)
	estado = models.IntegerField(default=0)
	insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre 
	#funcion para colorear estado de salas	
	def colorear(self):
		if self.estado == 1:
			return format_html(
				'<span style="color: #FF0000;">{}</span>',
					self.nombre,
				)

@python_2_unicode_compatible
class Solicitud(models.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	fecha = models.DateField('fecha solicitud')
	hora_inicio = models.DateTimeField('hora de inicio')
	hora_termino = models.DateTimeField('hora de termino')
	cantidad_personas = models.IntegerField(default=0)
	insumos = models.ManyToManyField(Insumo)
	sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
	def __str__(self):
		return self.sala