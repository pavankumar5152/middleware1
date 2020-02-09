from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    # print("the line added by view function")
    # return HttpResponse("<h1>Customer middleware Demo</h1>")
    print(10/0)
    return HttpResponse('<h1>Hello This is from home page view</h1>')
