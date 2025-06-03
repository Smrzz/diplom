from django.shortcuts import render

from .models import New

def news(request):
    news = New.objects.all()
    context = {
            'news': news
        }
    print(context)
    return render(request, 'news/news.html', context)