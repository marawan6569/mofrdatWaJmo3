from django.contrib import admin
from .models import Ques

# Register your models here.
class QuesAdmin(admin.ModelAdmin):
    list_display = ['highlighted_word', '__str__', 'created_at', 'active']
    search_fields = ['highlighted_word', 'verse']
    list_editable = ['active']
    filter_horizontal = ('answers',)
    actions = ['activate', 'deactivate']

    def activate(modeladmin, request, queryset):
        queryset.update(active=True)
    def deactivate(modeladmin, request, queryset):
        queryset.update(active=False)
admin.site.register(Ques, QuesAdmin)