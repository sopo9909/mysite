from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    # 그러면 이거를 보내줌
    return HttpResponse("Hello, world. You're at the polls index.")