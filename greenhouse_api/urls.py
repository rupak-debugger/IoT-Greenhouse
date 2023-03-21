from django.urls import include, path
from greenhouse_api import views

urlpatterns = [
    path('fetch_data', views.fetch_sensor_data, name='fetch_data'),
    path('post_data', views.save_sensor_data, name='post_data'),
]
