from django.http import HttpResponse
from django.db import transaction
from django.db import IntegrityError
from shop.models import Customer, Order, Payment


def sendemail():
    print("email sent successfully")


def create_customer():
    return Customer.objects.create(
        name="manzoora",
        email="manzoora@gmail.com"
    )


def create_order(customer):
    return Order.objects.create(
        customer=customer,
        total_amount=150007,
        status="CONFIRMED"
    )


def create_payment(order):
    return Payment.objects.create(
        order=order,
        amount=123490,
        status="SUCCESS"
    )


