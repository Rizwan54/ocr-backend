from django.urls import path
from . import views

urlpatterns = [
    path('generate-token/', views.MyTokenObtainPairView.as_view(), name="generate-token"),
]