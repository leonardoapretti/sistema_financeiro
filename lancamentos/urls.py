from django.urls import path
from lancamentos import views

app_name = 'lancamentos'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),
    path('novo/', views.novo, name='novo'),
    path('extrato/', views.extrato, name='extrato'),
    path('detalhes/<int:id_lancamento>/', views.detalhes, name='detalhes'),
    path('testes', views.testes, name='testes'),
]
