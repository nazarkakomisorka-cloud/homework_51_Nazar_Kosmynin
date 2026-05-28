from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cat/', views.cat_page, name='cat_page'),
]
