from django.contrib import admin

from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=("area","bedrooms","age","info","value")

admin.site.register(Service,ServiceAdmin)
# Register your models here.
