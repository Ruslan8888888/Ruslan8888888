from django.shortcuts import render


def index(request):
    return render(request,'rko/index.html')

def about(request):
    return render(request,'rko/about.html')

