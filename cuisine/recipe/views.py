from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    """
    Главная страница.
    """
    return render(request, 'recipe/base.html')


def recipe_detail(request):
    """
    Детальный просмотр информации о рецепте.
    """
    return render(request, 'recipe/recipe_detail.html')


@login_required
def user_recipes(request):
    """
    Просмотр рецептов добавленных пользователем
    """
    return render(request, 'recipe/user_recipes.html')
