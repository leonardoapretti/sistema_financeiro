from django.urls import path
from lancamentos import views
from django.contrib.auth.decorators import login_required
app_name = 'lancamentos'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),

    path('novo/', login_required(views.NewEntryView.as_view(),
                                 login_url='lancamentos:login_user', redirect_field_name='next'), name='novo'),
    path('lancamentos/extrato', login_required(views.ExtratoView.as_view(),
                                               login_url='lancamentos:login_user', redirect_field_name='next'), name='extrato'),
    path('<pk>/delete/', login_required(views.DeleteLancamentoView.as_view(),
                                        login_url='lancamentos:login_user', redirect_field_name='next'), name='delete'),
    path('<pk>/detalhes/', login_required(views.LancamentoView.as_view(),
                                          login_url='lancamentos:login_user', redirect_field_name='next'), name='detalhes'),
    path('<pk>/edit/', login_required(views.UpdateLancamentoView.as_view(),
                                      login_url='lancamentos:login_user', redirect_field_name='next'), name='edit'),
    path('<entry_id>/create_installment/', login_required(views.InstallmentCreateView.as_view(),
                                                          login_url='lancamentos:login_user', redirect_field_name='next'), name='create_installment'),
    path('parcelas/extrato/', login_required(views.InstallmentListView.as_view(),
                                             login_url='lancamentos:login_user', redirect_field_name='next'), name='installment_list'),
    path('testes', login_required(views.home, login_url='lancamentos:login_user',
         redirect_field_name='next'), name='testes'),

]
