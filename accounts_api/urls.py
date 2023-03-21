from accounts_api import views 
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns =[
    path('register_user', views.registration_view, name='register_from_api'),
    # path('log_in', obtain_auth_token, name='login_from_api'),
    # this is to be done later
]