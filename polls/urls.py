from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # mysite에서 넘어온 것을 views 인덱스로 보여줌
]