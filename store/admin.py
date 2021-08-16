from django.contrib import admin

from .models import *

# Registering our databases from models.py
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)