from django.urls import path
from .views import (
    WalletListCreateAPI,
    TransactionListAPI,
    DepositAPI,
    WithdrawAPI
)

urlpatterns = [
    path("wallets/", WalletListCreateAPI.as_view()),
    path("transactions/", TransactionListAPI.as_view()),
    path("deposit/", DepositAPI.as_view()),
    path("withdraw/", WithdrawAPI.as_view()),
]