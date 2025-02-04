from django.contrib import admin

from . import models

@admin.register(models.ZillowListing)
class ZillowListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'zillow_id', 'address', 'bedrooms', 'bathrooms', 'price', 'property_size', 'area_unit')
    list_filter = ('home_type', 'area_unit', 'rentzestimate_last_updated')
    search_fields = ('id', 'zillow_id', 'street')
    date_hierarchy = 'created_at'


    def address(self, obj):
        if obj is None:
            return None

        return f'{obj.street}, {obj.city}, {obj.state} {obj.zipcode}'
    address.short_description = 'Address'
