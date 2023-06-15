from accounts_api import views 
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns =[
    path('register_user', views.registration_view, name='register_from_api'),
    path('log_in', obtain_auth_token, name='login_from_api'),
    # path('login', views.login_user, name='login_api'),
    path('request_account', views.request_Account, name='request_account'),
    path('update_account', views.update_account, name='update_account'),
    path('change_password', views.change_password, name='change.password'),
    # this is to be done later
]