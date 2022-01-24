from django.urls import path 
from . import views

urlpatterns = [
    path('signup/', views.registerUser, name="register"),
    path('', views.getUsers, name="users"),

    path('delete/<str:pk>/', views.deleteUser, name='user-delete'),
]