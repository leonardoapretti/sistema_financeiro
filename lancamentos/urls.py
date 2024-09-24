from django.urls import path
from lancamentos import views
from django.contrib.auth.decorators import login_required
app_name = 'entries'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),

    path('novo/', views.NewEntryView.as_view(),
         name='new'),
    path('lancamentos/extrato', views.EntriesView.as_view(),
         name='extrato'),
    path('detalhes/<slug:slug>/', views.EntryView.as_view(),
         name='detalhes'),
    path('detalhes/<slug:slug>/edit/', views.EntryUpdateView.as_view(),
         name='entry_update'),
    path('<pk>/delete/', views.EntryDeleteView.as_view(),
         name='delete'),
    path('<entry_id>/create_installment/', views.InstallmentCreateView.as_view(),
         name='create_installment'),
    path('<pk>/update_installment/', views.InstallmentUpdateView.as_view(),
         name='installment_update'),
    path('parcelas/extrato/', views.InstallmentListView.as_view(),
         name='installment_list'),
    path('parcelas/quitar/', views.PayInstallmentView.as_view(),
         name='installment_pay'),
    #     path('parcelas/quitar/', views.PayInstallmentView.as_view(),
    #          name='installment_pay'),
    path('testes', views.testes, name='testes'),

]
