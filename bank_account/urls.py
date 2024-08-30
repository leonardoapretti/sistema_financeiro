from django.urls import path
from bank_account import views

app_name = 'bank_account'

urlpatterns = [
    path('', views.BankAccountFormView.as_view(),
         name='new'),
]
