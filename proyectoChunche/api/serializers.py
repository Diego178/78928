from rest_framework.serializers import ModelSerializer
from .models import Temperatura, CalidadAire

class TemperaturaSerializer(ModelSerializer):
    class Meta:
        model = Temperatura
        fields = '__all__'

class CalidadAireSerializer(ModelSerializer):
    class Meta:
        model = CalidadAire
        fields = '__all__'