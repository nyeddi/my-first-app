from django.contrib import admin
from bookmarks.models import *


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('url', 'description')
    search_fields = ('url', 'description', 'extended')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Bookmark, BookmarkAdmin)