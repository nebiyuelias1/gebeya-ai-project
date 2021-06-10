from django.contrib import admin

from views.models import View, ViewReview, Term


@admin.display(description='Name')
def full_name(obj):
    if obj.user:
        return "%s %s" % (obj.user.first_name, obj.user.last_name)


class TermInline(admin.TabularInline):
    model = Term


class ViewReviewAdmin(admin.ModelAdmin):
    inlines = [TermInline]


class ViewReviewInline(admin.StackedInline):
    model = ViewReview
    show_change_link = True
    inlines = [TermInline]
    readonly_fields = ('category_one_score', 'category_two_score', 'category_three_score')


class ViewAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('content', 'created_at', full_name, 'flagged')
    list_filter = ('flagged', 'user')
    ordering = ['-created_at']
    search_fields = ['content', 'user__first_name__icontains', 'user__last_name__icontains']
    view_on_site = True
    inlines = [ViewReviewInline]


admin.site.register(View, ViewAdmin)
admin.site.register(ViewReview, ViewReviewAdmin)
admin.site.register(Term)
