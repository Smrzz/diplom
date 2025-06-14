from django.shortcuts import render


def index(request):
    return render(request, 'home/home.html')


def ruk_view(request):
    return render(request, 'ruk.html')

def safe_view(request):
    return render(request, 'safe.html')

def turism_view(request):
    return render(request, 'turism.html')
