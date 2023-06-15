from greenhouse import views
from django.urls import include, path

urlpatterns = [
    path('', views.home, name="home"),
    path('relays', views.change_control_value, name="relay1"),
    path('histogram', views.histogram, name="histogram"),
]