from django.urls import path
from lancamentos import views

app_name = 'lancamentos'

urlpatterns = [
    path('', views.home, name='home'),
    path('testes', views.testes, name='testes'),
]
