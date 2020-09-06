from django.contrib import admin
from .models import Table, Order, ServicePercentage, Status

admin.site.register(Table)
admin.site.register(Order)
admin.site.register(ServicePercentage)
admin.site.register(Status)
