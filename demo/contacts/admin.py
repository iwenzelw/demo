from django.contrib import admin

from .models import Contact, Contact1


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)


class Contact1Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email',)
    list_per_page = 25


admin.site.register(Contact1, Contact1Admin)
