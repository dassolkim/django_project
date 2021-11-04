from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .serializers import HelloSerializer
from rest_framework.parsers import JSONParser

from .models import HelloWorld
# Create your views here.

def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        # return render(request, 'accountapp/hello_world.html',
        #               context={'hello_world_output': new_hello_world})
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'hello_world_list': hello_world_list})

def hello_object_list(request):
    if request.method == 'GET':
        ho = HelloWorld.objects.all()
        serializer = HelloSerializer(ho, many=True)
        return JsonResponse(serializer.data, safe=False)