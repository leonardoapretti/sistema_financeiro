from django.urls import path
from bank_account import views
from django.contrib.auth.decorators import login_required

app_name = 'bank_account'

urlpatterns = [
    path('instituicaofinanceira/nova/', views.BankAccountFormView.as_view(),
         name='new_bank_account'),
    path('cartao/novo/', views.CardFormView.as_view(),
         name='new_card'),
    path('cartoes/', views.CardListView.as_view(),
         name='cards'),
    path('bancos/', views.BankListView.as_view(),
         name='banks'),
    path('bancos/<pk>/apagar', views.BankDeleteView.as_view(),
         name='delete_bank'),
    path('cartoes/<pk>/apagar', views.CardDeleteView.as_view(),
         name='delete_card'),

]
