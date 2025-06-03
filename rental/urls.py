from django.urls import path
from rental import views

urlpatterns = [
    path('', views.rental, name='rental'),  # Прокат страница
]