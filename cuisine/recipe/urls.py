from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('detail/', views.recipe_detail, name='detail'),
    path('list/', views.user_recipes, name='list'),
]
