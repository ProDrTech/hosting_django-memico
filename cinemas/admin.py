from django.contrib import admin
from django.forms import DecimalField
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import *
# Register your models here.

class CinemaArchivesInlines(admin.TabularInline):
    model = CinemaArchives

class CinemaGenresInlines(admin.TabularInline):
    model = CinemaGenres

class CinemaCountryInlines(admin.TabularInline):
    model = CinemaCountry

class CinemaProductComponyInlines(admin.TabularInline):
    model = CinemaProductCompony

class CinemaDirectersInlines(admin.TabularInline):
    model = CinemaDirecters

class CinemaReleaseDateInlines(admin.TabularInline):
    model = CinemaReleaseDate

class CinemaStarsInlines(admin.TabularInline):
    model = CinemaStars

class CinemaTagsInlines(admin.TabularInline):
    model = CinemaTags

class CinemaImagesInlines(admin.TabularInline):
    model = CinemaImages

class CinemaPhotosInlines(admin.TabularInline):
    model = CinemaPhotos

class CinemaAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating', 'duration', 'description', 'language', 'category', 'created_at']
    formfield_overrides = {
        models.DecimalField: {
            'form_class': DecimalField,
            'min_value': 0.0,
            'max_value': 10.0,
        }
    }
    inlines = [CinemaArchivesInlines, CinemaGenresInlines, CinemaCountryInlines, CinemaProductComponyInlines, CinemaDirectersInlines, CinemaReleaseDateInlines, CinemaStarsInlines, CinemaTagsInlines, CinemaImagesInlines, CinemaPhotosInlines]

admin.site.register(Cinemas, CinemaAdmin)
admin.site.register(CinemaArchives)
admin.site.register(CinemaGenres)
admin.site.register(CinemaComents)
admin.site.register(CinemaCountry)
admin.site.register(CinemaProductCompony)
admin.site.register(CinemaDirecters)
admin.site.register(CinemaReleaseDate)
admin.site.register(CinemaStars)
admin.site.register(CinemaTags)
admin.site.register(CinemaImages)
admin.site.register(Category)
admin.site.register(CinemaPhotos)