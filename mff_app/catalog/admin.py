from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'country')
    search_fields = ('title', 'country')
    list_filter = ('category', 'genre')
    list_per_page = 20
    fieldsets = (
        ('Основная информация', {
            'fields': ('category', 'title', 'slug', 'release', 'country', 'genre')
        }),
        ('Расширенная информация', {
            'fields': ('director', 'actors', 'description')
        }),
        ('Ссылка на изображение', {
            'fields': ('img_url',)
        }),
    )
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'is_viewed')
