from unicodedata import name
from accounts import views
from django.urls import path

urlpatterns = [
    path('login', views.login_user, name='login_user'),
    path('', views.form, name='form'),
    path('logout', views.logout_user, name="logout")
]
