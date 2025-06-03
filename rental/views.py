from django.shortcuts import render


def rental(request):
    return render(request, 'rental/rental.html')