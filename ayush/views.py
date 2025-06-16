from django.shortcuts import render


# Create your views here.
def all_ayush(request):
    return render(request, 'ayush/all_ayush.html')