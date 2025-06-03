from django.urls import path
from hostels import views

urlpatterns = [
    path('', views.hostels, name='hostels'),
    path('book/', views.book_room, name='book_room'),
]
