from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('ruk', views.ruk_view, name='ruk'),   
    path('safe', views.safe_view, name='safe'), 
    path('turism', views.turism_view, name='turism'), 
    ]