from django.urls import path
from . import views

urlpatterns = [
    path('coin/<int:num>/', views.gen_coin, name='gen_coin'),
    path('dice/<int:num>/', views.gen_dice, name='gen_dice'),
    path('number/<int:num>/', views.gen_number, name='gen_number'),
    path('games/', views.select_game, name='select_game'),
]