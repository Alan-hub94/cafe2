from django.contrib import admin
from .models import Service, Service

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, ServiceAdmin)

