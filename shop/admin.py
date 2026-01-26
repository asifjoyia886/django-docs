from django.contrib import admin

from shop.models import Order,Customer,Payment
# Register your models here.


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Payment)