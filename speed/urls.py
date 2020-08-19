from .views import RegisterAPI, ClientApi
from django.urls import path

app_name = 'speed'

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/client/', ClientApi.as_view(), name='client'),
]