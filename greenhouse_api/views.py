from django.http import JsonResponse
from greenhouse.models import SensorData, RelayControl
from greenhouse_api.serializers import SensorDataSerializer, RelayControlSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@api_view(['POST', ])
@csrf_exempt
@permission_classes([AllowAny])
def save_sensor_data(request):
    if request.method == "POST":
        serialized_data = SensorDataSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            qudata = RelayControl.objects.get(id=1)
            sudata = RelayControlSerializer(qudata)
            jdata = JSONRenderer().render(sudata.data)
            return HttpResponse(jdata)
        else:
            return JsonResponse(serialized_data.errors, safe=False)


@api_view(['GET', ])
@permission_classes([AllowAny])
def fetch_sensor_data(request):
    if request.method == "GET":
        try:
            qdata = SensorData.objects.last()
            sdata = SensorDataSerializer(qdata)
            jdata = JSONRenderer().render(sdata.data)
            return HttpResponse(jdata, content_type='application/json')

        except SensorData.DoesNotExist:
            error = {'error': 'Requested Data Not Found.'}
            return JsonResponse(error, safe=False,)
