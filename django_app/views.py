from django import setup
import os

from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Memo
from . import forms

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoDocker.settings')
setup()

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
    memos = Memo.objects.all()
    # return render(request, 'memo.html', context={'memo': 'Memo Page'})
    # for memo in memos:
    #     print(memo.memo)
    return render(request, 'memo.html', context={'memos': memos})


def new_memo(request):
    new_memo = forms.MemoForm()
    if request.method == 'POST':
        new_memo = forms.MemoForm(request.POST)
        print('--------- post --------------------')
        print(new_memo)
        # バリデーション実行後、保存
        if new_memo.is_valid():
            print('--------- validation and save ------------------')
            new_memo.save()
            # ホーム画面に遷移
            return redirect('django_app:memo')

    return render(request, 'new_memo.html', context={'new_memo': new_memo})
