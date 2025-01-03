from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *

def main_page(request):
    """
    Главная страница: список категорий
    """
    categories = Category.objects.all()
    return render(request, 'main.html', {'categories': categories})


def get_all_films(request):
    """
    Получение всех фильмов
    """
    films = Film.objects.all().order_by('-created_at')
    return render(request, 'films.html', {'films': films})


def get_films_by_category(request, category_slug):
    """
    Получение списка фильмов по категории
    """
    category = Category.objects.get(slug=category_slug)
    films = category.film_set.all()
    return render(request,
                  'films_by_category.html',
                  {'category': category, 'films': films})