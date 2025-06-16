from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello This is django")
    return render(request, 'admin/index.html')

def about_us(request):
    print("followings")
    # print(request.method)
    # print(request)
    return HttpResponse("About us")
