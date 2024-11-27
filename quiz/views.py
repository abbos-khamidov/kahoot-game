from django.shortcuts import render
from django.http import JsonResponse
from .models import Question

def get_questions(request):
    questions = Question.objects.all()
    question_list = [
        {
            'id': q.id,
            'text': q.text,
            'options': [q.option1, q.option2, q.option3, q.option4],
            'correct': [q.option1, q.option2, q.option3, q.option4][q.correct_option - 1]
        }
        for q in questions
    ]
    return JsonResponse({'questions': question_list})
