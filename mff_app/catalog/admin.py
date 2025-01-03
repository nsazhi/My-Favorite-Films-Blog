from django.contrib import admin
from .models import *

admin.site.register(Category)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', )
    list_filter = ('category', 'genre', 'country')
    list_per_page = 20
    fieldsets = (
        ('Основная информация', {
            'fields': ('category', 'title', 'release', 'country', 'genre')
        }),
        ('Расширенная информация', {
            'fields': ('director', 'actors', 'description')
        }),
        ('Ссылка на изображение', {
            'fields': ('img_url', )
        }),
    )
    readonly_fields = ('slug', 'is_viewed')
