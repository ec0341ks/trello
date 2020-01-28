from django.contrib.auth import login  # 追加
from django.contrib.auth.forms import UserCreationForm  # 追加
from django.shortcuts import render, redirect  # redirectをインポート


# # Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "trello/index.html")


def home(request):
    return render(request, "trello/home.html")


def signup(request):
    if request.method == 'POST':
        print("会員照合するだよ")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("trello:home")

    else:
        print('elseだよ')
        print(request)
        context = {
            "form": UserCreationForm()
        }
        print(context)
        return render(request, 'trello/signup.html', context)
