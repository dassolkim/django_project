from django.urls import path, include

from .views import hello_world, AccountCreateView
from .views import hello_object_list

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('hello_list/', hello_object_list, name='hello_object_list'),
    # 함수형 view와의 차이점: 이름을 바로 쓸 수 없음
    path('create/', AccountCreateView.as_view(), name='create')
]