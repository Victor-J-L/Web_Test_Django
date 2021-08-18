from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('shop/', views.products),
    path('user/', views.costumer),
]