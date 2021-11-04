from django.urls import path, include

from .views import hello_world
from .views import hello_object_list

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('hello_list/', hello_object_list, name='hello_object_list')
]