from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .models import Temperatura, CalidadAire
from .serializers import TemperaturaSerializer, CalidadAireSerializer

@api_view(['GET'])
def getTemperatura(request):
    temperatura = Temperatura.objects.all()
    serializer = TemperaturaSerializer(temperatura, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getHola(request):
    return Response("hola")

@api_view(['POST'])
def postTemperatura(request):
    data = request.data
    temperatura = Temperatura.objects.create(
        temperaturaC = data['temperaturaC'],
        temperaturaF = data['temperaturaF'],
        humedad = data['humedad'],
        calorC = data['calorC'],
        calorF = data['calorF'],
    )
        
    serializer = TemperaturaSerializer(temperatura, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def getCalidadAire(request):
    calidad = CalidadAire.objects.all()
    serializer = CalidadAireSerializer(calidad, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getTemperaturaUltimo(request):
    
    ultimaTemperatura = Temperatura.objects.last()
    data = {'id': ultimaTemperatura.id,
            'temperaturaC': ultimaTemperatura.temperaturaC,
            'temperaturaF': ultimaTemperatura.temperaturaF,
            'humedad': ultimaTemperatura.humedad,
            'calorC': ultimaTemperatura.calorC,
            'calorF': ultimaTemperatura.calorF}
    return JsonResponse(data)

@api_view(['POST'])
def postCalidadAire(request):
    data = request.data
    calidad = CalidadAire.objects.create(
        amoniaco = data['amoniaco'],
        benceno = data['benceno'],
        alcohol = data['alcohol'],
        co2 = data['co2'],
        nitrogeno = data['nitrogeno'],
        monoxido = data['monoxido'],
    )
        
    serializer = CalidadAireSerializer(calidad, many = False)
    return Response(serializer.data)

# @api_view(['PUT'])
# def putEmployee(request, pk):
#     data = request.data
#     employee = Employee.objects.get(id=pk)
#     serializer = EmployeesSerializer(instance=employee, data = data)
#     if(serializer.is_valid()):
#         serializer.save()
#     return Response(serializer.data)
    
# @api_view(['DELETE'])
# def deleteEmployee(request, pk):
#     employee = Employee.objects.get(id=pk)
#     employee.delete()
#     return Response('Empleado eliminado')