from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('about/', views.about, name='about'),
]
