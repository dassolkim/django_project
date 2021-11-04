from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .decorators import account_ownership_required
from .forms import AccountUpdateForm
from .serializers import HelloSerializer
from rest_framework.parsers import JSONParser

from .models import HelloWorld

has_ownership = [account_ownership_required, login_required]

# Create your views here.
# django에서 제공하는 login 제한 조건, decorator 한줄로 적용 가능
@login_required
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
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})



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

# 일반 function에 사용하는 decorator를 class 내 method에 적용할 수 있도록 변환해줌

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
# 4줄짜리를 2 줄로 줄일 수 있
# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'