from django.shortcuts import render
from django.core.paginator import Paginator
from app.models import Qstion, User, Answer, Tags

tags = [{'id' : 0, 'text' : 'bender'}, {'id' : 1, 'text' : 'black-jack'}, {'id' : 2, 'text' : 'best'}]

def index(request):
    context = paginate(Qstion.objects.all(), request, 3)

    return render(request, 'index.html', context)

def ask(request):
    return render(request, 'ask.html', {})

def listing_q(request, pk):
    context = paginate(Qstion.objects.filter(tag=pk), request, 3)
    context['tag'] = Tags.objects.get(pk=pk).designation

    return render(request, 'listing_q.html', context)

def question(request, pk):
    context = paginate(Answer.objects.filter(question_id=pk), request, 3)
    context['question'] = Qstion.objects.get(pk = pk)
    return render(request, 'question.html', context)

def hot(request):
    context = paginate(Qstion.objects.all(), request, 3)
    return render(request, 'hot_questions.html', context)

def login(request):
    return render(request, 'login.html', {})

def settings(request):
    return render(request, 'settings.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def paginate(objects_list, request, per_page):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return context
