# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Search, Email, Influencer, NicheList, OrderedList, Profile

# Register your models here.
admin.site.register(Influencer)
admin.site.register(NicheList)
admin.site.register(Profile)

class SearchAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('search', 'created')
    list_display_links = ('search', 'created')

admin.site.register(Search, SearchAdmin)

class EmailAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('email', 'created')
    list_display_links = ('email', 'created')

admin.site.register(Email, EmailAdmin)

class OrderedListAdmin(admin.ModelAdmin):
    list_display = ('list', 'influencers', 'order')
    list_display_links = ('list', 'influencers', 'order')

admin.site.register(OrderedList, OrderedListAdmin)