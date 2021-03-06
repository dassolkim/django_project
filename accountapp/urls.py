from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, HelloList, \
    HelloListViewset
from .views import hello_object_list

app_name = "accountapp"

# viewSet test

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('hello_list/', hello_object_list, name='hello_object_list'),
    path('list_api/', HelloList.as_view(), name='hello_obj_list'),
    # 함수형 view와의 차이점: 이름을 바로 쓸 수 없음
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete')

]