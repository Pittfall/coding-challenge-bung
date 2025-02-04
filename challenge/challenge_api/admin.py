from django.contrib import admin
from . import models

admin.site.register(models.ZillowListing)
class ZillowListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rentzestimate_amount', 'rentzestimate_last_updated')
    list_filter = ('rentzestimate_last_updated',)
    search_fields = ('zillow_id', 'street')
