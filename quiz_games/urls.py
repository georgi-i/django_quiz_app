from django.urls import path
from quiz_games import views

urlpatterns = [
    path("", views.home, name="home"),
    path("easy/", views.easy, name="easy"),
    path("medium/", views.medium, name="medium"),
    path("hard/", views.hard, name="hard")
]

