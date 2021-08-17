from quiz_games.models import Question
from django.views.generic import TemplateView
#import requests

class HomeView(TemplateView):
    template_name = "quiz_games/home.html"

class QuestionsView(TemplateView):
    template_name = "quiz_games/questions.html"

    def get_context_data(self, **kwargs):
        difficulty = self.request.path.replace('/','')
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.order_by('?').filter(difficulty=difficulty)[:10]

        return context



#For DB populating

#def get_questions(difficulty):
#    url = f'https://opentdb.com/api.php?amount=10&category=9&difficulty={difficulty}&type=multiple'
#    response = requests.get(url)
#    data = response.json()
#    questions = data['results']
#
#    for q in questions:
#        question_data = Question( 
#                                difficulty = difficulty,
#                                category = q['category'],
#                                type = q['type'],
#                                question = q['question'],
#                                correct_answer = q['correct_answer'],
#                                incorrect_answer_one = q['incorrect_answers'][0],
#                                incorrect_answer_two = q['incorrect_answers'][1],
#                                incorrect_answer_three = q['incorrect_answers'][2],
#                                )
#        question_data.save() 
#    
#    return Question.objects.all()[:10]