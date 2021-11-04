from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .forms import AccountUpdateForm
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


# Class Based View, 상당히 간편하고 직관적
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # reverse는 호출 방식의 차이로 class에서 그대로 사용 불가용(함수형 view에서 사용)
    # reverse_lazy는 class형 view에서 사용
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'