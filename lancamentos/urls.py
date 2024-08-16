from django.urls import path
from lancamentos import views

urlpatterns = [
    path('', views.home),
]
