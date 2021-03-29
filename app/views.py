from django.shortcuts import render

questions = [
    {
        'id': idx,
        'title': f'Title number {idx}',
        'text': f'Some text for question #{idx}'
    } for idx in range(10)
]

answers = [
    {
        'id': idx,
        'text': f'Some text for answer #{idx}'
    } for idx in range(5)
]

tags = [{'id' : 0, 'text' : 'bender'}, {'id' : 1, 'text' : 'black-jack'}, {'id' : 2, 'text' : 'best'}]

def index(request):
    return render(request, 'index.html', {'questions' : questions})

def ask(request):
    return render(request, 'ask.html', {})

def listing_q(request, pk):
    cur_tag = tags[pk]
    return render(request, 'listing_q.html', {'questions' : questions, 'tags' : cur_tag})

def question(request, pk):
    cur_question = questions[pk]
    return render(request, 'question.html', {'answers' : answers, 'question' : cur_question})

def hot(request):
    return render(request, 'hot_questions.html', {'questions' : questions})

def login(request):
    return render(request, 'login.html', {})

def settings(request):
    return render(request, 'settings.html', {})

def signup(request):
    return render(request, 'signup.html', {})