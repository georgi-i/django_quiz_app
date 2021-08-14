from quiz_games.models import Question
from django.shortcuts import render
import requests

def home(request):
    return render(request, "quiz_games/home.html")

def get_question(difficulty):
    url = f'https://opentdb.com/api.php?amount=10&category=9&difficulty={difficulty}&type=multiple'
    response = requests.get(url)
    data = response.json()
    questions = data['results']

    for q in questions:
        question_data = Question( 
                                difficulty = difficulty,
                                category = q['category'],
                                type = q['type'],
                                question = q['question'],
                                correct_answer = q['correct_answer'],
                                incorrect_answer_one = q['incorrect_answers'][0],
                                incorrect_answer_two = q['incorrect_answers'][1],
                                incorrect_answer_three = q['incorrect_answers'][2],
                                )
        question_data.save() 
    
    return Question.objects.all()[:10]


def easy(request):

    questions = get_question('easy')    

    return render(request, "quiz_games/questions.html", { "questions": questions})

def medium(request):

    questions = get_question('medium')    

    return render(request, "quiz_games/questions.html", { "questions": questions})

def hard(request):
        
    questions = get_question('hard')    

    return render(request, "quiz_games/questions.html", { "questions": questions})
