from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from application.models.configuration.config import Config as AdminModel


class Admin(SimpleHistoryAdmin):
    list_display = ('key', 'value')
    list_display_links = ('key',)
    search_fields = ('key',)
    list_per_page = 25


admin.site.register(AdminModel, Admin)
