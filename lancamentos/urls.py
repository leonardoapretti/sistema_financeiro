from django.urls import path
from lancamentos import views
from django.contrib.auth.decorators import login_required
app_name = 'lancamentos'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),

    path('novo/', login_required(views.NovoLancamentoView.as_view(),
                                 login_url='lancamentos:login_user', redirect_field_name='next'), name='novo'),
    path('extrato/', login_required(views.ExtratoView.as_view(),
                                    login_url='lancamentos:login_user', redirect_field_name='next'), name='extrato'),
    path('<pk>/delete/', login_required(views.DeleteLancamentoView.as_view(),
                                        login_url='lancamentos:login_user', redirect_field_name='next'), name='delete'),
    path('<pk>/detalhes/', login_required(views.LancamentoView.as_view(),
                                          login_url='lancamentos:login_user', redirect_field_name='next'), name='detalhes'),
    path('<pk>/edit/', login_required(views.UpdateLancamentoView.as_view(),
                                      login_url='lancamentos:login_user', redirect_field_name='next'), name='edit'),
    path('testes', login_required(views.GenericFormView.as_view(
    ), login_url='lancamentos:login_user', redirect_field_name='next'), name='testes'),

]
