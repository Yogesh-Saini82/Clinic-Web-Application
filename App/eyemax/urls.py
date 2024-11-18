from django.urls import path
from eyemax import views


urlpatterns = [
    path('', views.index, name='index'),
]
