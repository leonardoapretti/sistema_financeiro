from django.urls import path
from lancamentos import views

app_name = 'lancamentos'

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('novo/', views.novo, name='novo'),
    path('testes', views.testes, name='testes'),
]
