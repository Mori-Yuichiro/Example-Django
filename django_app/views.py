from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse(f'<h1>Good</h1>')


def home(request, user_name):
    career = {
        'high_school': f'{ user_name }',
        'university': f'Kagawa {user_name}'
    }
    return render(request, 'home.html', context={'user_name': user_name, 'career': career})


def memo(request):
    return render(request, 'memo.html', context={'memo': 'Memo Page'})
