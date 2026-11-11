from django.db import models

class Raza(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Raza")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Raza"
        verbose_name_plural = "Razas"


class Ternero(models.Model):
    numero_identificador = models.CharField(max_length=50, unique=True, verbose_name="Número de Arete")
    peso_kg = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Peso (kg)")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    disponible_venta = models.BooleanField(default=True, verbose_name="¿Disponible para Venta?")
    precio_estimado = models.IntegerField(verbose_name="Precio Estimado ($)")
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE, related_name='terneros', verbose_name="Raza")

    def __str__(self):
        return f"Arete {self.numero_identificador} - {self.raza.nombre}"

    class Meta:
        verbose_name = "Ternero"
        verbose_name_plural = "Terneros"