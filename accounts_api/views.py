from accounts_api.serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your views here.


@api_view(['POST', ])
@authentication_classes([]) #disables authentication
@permission_classes([]) #disables permissions
def registration_view(request):

    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'User Registered Successfully. ' + account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
            # data['email'] = account.email
            # data['username'] = account.username
        else:
            data = serializer.errors

        return JsonResponse(data, safe=False)
