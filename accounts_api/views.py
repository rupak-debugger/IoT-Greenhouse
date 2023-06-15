from accounts.models import Account
from accounts_api.serializers import UserRegistrationSerializer, AccountRequestSerializer, ChangePasswordSerializer
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse, JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


@api_view(['POST', ])
@permission_classes([AllowAny])
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
            return JsonResponse(data, safe=False)
        else:
            data = serializer.errors
            return JsonResponse(data, safe=False)


# @api_view(["POST", ])
# @permission_classes([AllowAny])
# def login_user(request):
#     serializer = LoginSerializer(data=request.data)
#     if serializer.is_valid:
#         return HttpResponse('up to here')


@api_view(['GET', ])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def request_Account(request):

    try:
        account = request.user
    except Account.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, safe=False)

    serialized = AccountRequestSerializer(account)
    return JsonResponse(serialized.data, safe=False)


@api_view(['PUT', ])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def update_account(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, safe=False)
    if request.method == 'PUT':
        sdata = AccountRequestSerializer(account, data=request.data)
        if sdata.is_valid():
            sdata.save()
            return HttpResponse('updated successfully')
        return HttpResponse(sdata.errors)


@api_view(['PUT', ])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def change_password(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return JsonResponse(status=status.HTTP_404_NOT_FOUND, safe=False)
    if request.method == "PUT":
        sdata = ChangePasswordSerializer(account, data=request.data)
        if sdata.is_valid():
            # return HttpResponse('up to here')
            changed = sdata.save()
            return HttpResponse(changed)
        return JsonResponse(sdata.errors, safe=False)
