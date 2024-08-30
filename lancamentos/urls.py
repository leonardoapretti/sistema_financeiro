from django.urls import path
from lancamentos import views
from bank_account import views as viewsAc

app_name = 'lancamentos'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),

    path('novo/', views.NovoLancamentoView.as_view(), name='novo'),
    path('extrato/', views.ExtratoView.as_view(), name='extrato'),
    path('<pk>/delete/', views.DeleteLancamentoView.as_view(), name='delete'),
    path('<pk>/detalhes/', views.LancamentoView.as_view(), name='detalhes'),
    path('<pk>/edit/', views.UpdateLancamentoView.as_view(), name='edit'),
    path('testes', views.GenericFormView.as_view(), name='testes'),

]
