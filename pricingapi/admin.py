from django.contrib import admin
from pricingapi import models
# Register your models here.

@admin.register(models.DecimalBasePrice)
class DBPAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'distance', 'enable']
    list_editable = ['price', 'distance', 'enable']
    list_per_page = 20
    exclude = ['enable']

    def save_model(self, request, obj, form, change) -> None:
        if obj.enable:
            enabled_obj = models.DecimalBasePrice.objects.filter(enable=True).first()
            if enabled_obj:
                enabled_obj.enable = False
                enabled_obj.save()

        return super().save_model(request, obj, form, change)
    
@admin.register(models.DistanceAdditionalPrice)
class DAPAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'distance', 'enable']
    list_editable = ['price', 'distance', 'enable']
    list_per_page = 20
    exclude = ['enable']

    def save_model(self, request, obj, form, change) -> None:
        if obj.enable:
            enabled_obj = models.DistanceAdditionalPrice.objects.filter(enable=True).first()
            if enabled_obj:
                enabled_obj.enable = False
                enabled_obj.save()

        return super().save_model(request, obj, form, change)

@admin.register(models.TimeMultiplierFactor)
class TMFAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'multiple_factor', 'enable']
    list_editable = ['time', 'multiple_factor', 'enable']
    list_per_page = 20
    exclude = ['enable']

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact_info']
    list_editable = ['name', 'contact_info']
    list_per_page = 20
    exclude = ['enable']

@admin.register(models.Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'vechile_id']
    list_editable = ['name', 'vechile_id']
    list_per_page = 20
    exclude = ['enable']