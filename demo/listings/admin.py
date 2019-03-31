from django.contrib import admin

from .models import Listing, District, Bedrooms, State


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'old_price', 'bedrooms', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'bedrooms',)
    list_editable = ('is_published',)
    search_fields = ('title', 'district', 'bedrooms', 'state', 'list_date', 'price')
    list_per_page = 25


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'district')


class BedroomsAdmin(admin.ModelAdmin):
    list_display = ('id', 'bedrooms')


admin.site.register(Listing, ListingAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Bedrooms, BedroomsAdmin)
admin.site.register(State)
