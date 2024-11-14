from django.urls import path
from eyemax import views
from .views import book_appointment, appointment_list

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', book_appointment, name='book_appointment'),
    path('appointments/', appointment_list, name='appointment_list'),
]
