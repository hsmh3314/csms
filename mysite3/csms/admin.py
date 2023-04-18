from django.contrib import admin
from .models import Customer, Service

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['ccode']

class ServiceAdmin(admin.ModelAdmin):
    search_fields = ['ccode']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Service, ServiceAdmin)
