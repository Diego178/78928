from django.db import models

class Temperatura(models.Model):
    id = models.IntegerField(primary_key=True)
    temperaturaC = models.IntegerField()
    temperaturaF = models.IntegerField()
    humedad = models.IntegerField()
    calorC = models.IntegerField()
    calorF = models.IntegerField()

class CalidadAire(models.Model):
    id = models.IntegerField(primary_key=True)
    amoniaco = models.IntegerField()
    benceno = models.IntegerField()
    alcohol = models.IntegerField()
    co2 = models.IntegerField()
    nitrogeno = models.IntegerField()
    monoxido = models.IntegerField()
