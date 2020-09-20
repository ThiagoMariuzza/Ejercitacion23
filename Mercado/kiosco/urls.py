from django.urls import path, include
from kiosco.views import HomeView

urlpatterns = [
    path('',HomeView.as_view(), name='home')
]