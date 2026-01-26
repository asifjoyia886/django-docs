from django.urls import path

from shop.views import first_transaction_case

urlpatterns = [
    path('transaction/',first_transaction_case,name='transacton'),
]
