from django.contrib import admin
from .models import *
# Register your models here.

class NewsCategoryInlines(admin.TabularInline):
    model = NewsCategory

class NewsTagsInlines(admin.TabularInline):
    model = NewsTags

class NewsArchivesInlines(admin.TabularInline):
    model = NewsArchives

class NewsAdmin(admin.ModelAdmin):
    list_display = ['date', 'title', 'description', 'image']
    inlines = [NewsCategoryInlines, NewsTagsInlines, NewsArchivesInlines]

admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory)
admin.site.register(NewsComents)
admin.site.register(NewsTags)
admin.site.register(NewsArchives)