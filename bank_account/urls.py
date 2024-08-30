from django.urls import path
from bank_account import views
from django.contrib.auth.decorators import login_required

app_name = 'bank_account'

urlpatterns = [
    path('instituicaofinanceira/nova/', login_required(views.BankAccountFormView.as_view(), login_url='lancamentos:login_user', redirect_field_name='next'),
         name='new_bank_account'),
    path('cartao/novo/', login_required(views.CardFormView.as_view(),
                                        login_url='lancamentos:login_user', redirect_field_name='next'), name='new_card'),
    path('cartoes/', login_required(views.CardListView.as_view(),
                                    login_url='lancamentos:login_user', redirect_field_name='next'), name='cards'),
    path('bancos/', login_required(views.BankListView.as_view(),
                                   login_url='lancamentos:login_user', redirect_field_name='next'), name='banks'),
    path('bancos/<pk>/apagar', login_required(views.BankDeleteView.as_view(),
                                              login_url='lancamentos:login_user', redirect_field_name='next'), name='delete_bank'),
    path('cartoes/<pk>/apagar', login_required(views.CardDeleteView.as_view(),
                                               login_url='lancamentos:login_user', redirect_field_name='next'), name='delete_card'),

]
