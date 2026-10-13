from django.db import models

class Plan(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()
	duracion_dias = models.PositiveIntegerField()
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre


class Socio(models.Model):
	plan = models.ForeignKey(
		Plan,
		on_delete=models.PROTECT,
		related_name="socios",
	)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	correo = models.EmailField(unique=True)
	telefono = models.CharField(max_length=20)
	fecha_inscripcion = models.DateField(auto_now_add=True)
	mensualidad = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return f"{self.nombre} {self.apellido}"
