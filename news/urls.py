from django.urls import path
from news import views

urlpatterns = [
    path('', views.news, name='news'),  # Новости страница
]