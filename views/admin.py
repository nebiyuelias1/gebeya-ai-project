from django.contrib import admin
from django.urls import reverse

from views.models import View


@admin.display(description='Name')
def full_name(obj):
    if obj.user:
        return "%s %s" % (obj.user.first_name, obj.user.last_name)


class ViewAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('content', 'created_at', full_name, 'flagged')
    list_filter = ('flagged', 'user')
    ordering = ['-created_at']
    search_fields = ['content', 'user__first_name__icontains', 'user__last_name__icontains']
    view_on_site = True

admin.site.register(View, ViewAdmin)
