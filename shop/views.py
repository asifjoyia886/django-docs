from django.http import HttpResponse
from django.db import transaction
from shop.helpers import create_customer, create_order, create_payment

def sendemail():
    print('email sent successfully')
def first_transaction_case(request):
    try:
        with transaction.atomic():
            customer = create_customer()
            order = create_order(customer)
            payment = create_payment(order)

            transaction.on_commit(sendemail)  # ✅ FIXED

        return HttpResponse("Transaction successful")

    except Exception:
        return HttpResponse("Transaction failed!")
