from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    country = models.CharField(max_length=100, verbose_name="País")

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Marca")
    model = models.CharField(max_length=100, verbose_name="Modelo")
    year = models.IntegerField(verbose_name="Año")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")

    def __str__(self):
        return f'{self.brand.name} {self.model}'

class Owner(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Coche")

    def __str__(self):
        return self.name
