from django.urls import path
from quiz_games.views import Home
from quiz_games.views import QuestionsView

urlpatterns = [
    path("", Home.as_view(template_name="quiz_games/home.html"), name="home"),
    path('easy/', QuestionsView.as_view(template_name="quiz_games/questions.html"), name='easy'),
    path('medium/', QuestionsView.as_view(template_name="quiz_games/questions.html"), name='medium'),
    path('hard/', QuestionsView.as_view(template_name="quiz_games/questions.html"), name='hard'),
]

