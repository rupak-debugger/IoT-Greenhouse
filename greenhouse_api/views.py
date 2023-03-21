from django.http import JsonResponse
from greenhouse.models import SensorData
from greenhouse_api.serializers import SensorDataSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework import status
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.


@api_view(['POST', ])
# # if we want authentication from IoT device
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
# if we don't want authentication from IoT device
@authentication_classes([])  # disables authentication
@permission_classes([])  # disables permissions
def save_sensor_data(request):
    if request.method == "POST":
        serialized_data = SensorDataSerializer(data=request.data)
        data = {}
        if serialized_data.is_valid():
            serialized_data.save()
            data['message'] = "Data saved to Database. "
    return JsonResponse(data, safe=False)


@api_view(['GET', ])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def fetch_sensor_data(request):
    if request.method == "GET":
        try:
            qdata = SensorData.objects.last()
            sdata = SensorDataSerializer(qdata)
            return JsonResponse(sdata.data, safe=False,)

        except SensorData.DoesNotExist:
            error = {'error': 'Requested Data Not Found.'}
            return JsonResponse(error, safe=False,)


# @api_view(['GET', ])
# def sensor_next_data(request, slug):
#     try:
#         qdata = SensorData.objects.get(slug=slug)
#     except SensorData.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         sdata = SensorDataSerializer(qdata)
#         jdata = JSONRenderer().render(sdata.data)
#         return HttpResponse(jdata, content_type='application/json')
