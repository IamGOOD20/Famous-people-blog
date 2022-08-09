from django.contrib import admin

from .models import *



class StarsAdmin(admin.ModelAdmin):
      list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
      list_display_links = ('id', 'title')
      search_fields = ('title', 'content')
      list_editable = ('is_published',) # makes the field editable
      list_filter = ('is_published', 'time_create')


class CategoryAdmin(admin.ModelAdmin):
      list_display = ('id', 'name')
      list_display_links = ('id', 'name')
      search_fields = ('name',)


admin.site.register(Stars, StarsAdmin)
admin.site.register(Category, CategoryAdmin)