from django.contrib import admin
from .models import LibraryItem


class LibraryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year_published', 'rating', 'created_at')
    list_filter = ('author', 'year_published')
    search_fields = ('title', 'author')
    ordering = ('-created_at',)

admin.site.register(LibraryItem, LibraryItemAdmin)