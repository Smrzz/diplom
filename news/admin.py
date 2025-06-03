from django.contrib import admin
from .models import New

@admin.register(New)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)