from django.urls import path
from lancamentos import views
from django.contrib.auth.decorators import login_required
app_name = 'lancamentos'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),

    path('novo/', views.NewEntryView.as_view(),
         name='novo'),
    path('lancamentos/extrato', views.EntriesView.as_view(),
         name='extrato'),
    path('<pk>/delete/', views.EntryDeleteView.as_view(),
         name='delete'),
    path('<pk>/detalhes/', views.EntryView.as_view(),
         name='detalhes'),
    path('<pk>/edit/', views.EntryUpdateView.as_view(),
         name='edit'),
    path('<entry_id>/create_installment/', views.InstallmentCreateView.as_view(),
         name='create_installment'),
    path('parcelas/extrato/', views.InstallmentListView.as_view(),
         name='installment_list'),
    path('parcelas/quitar/', views.PayInstallmentView.as_view(),
         name='installment_pay'),
    #     path('parcelas/quitar/', views.PayInstallmentView.as_view(),
    #          name='installment_pay'),
    path('testes', views.testes, name='testes'),

]
