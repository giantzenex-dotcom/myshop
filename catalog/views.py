from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
    return HttpResponse("<h1>გამარჯობა!</h1>")
def about(request):
    return HttpResponse("<h1>მე გიორგი ვარ</h1>")