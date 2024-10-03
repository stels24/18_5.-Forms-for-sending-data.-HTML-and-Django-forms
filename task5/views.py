from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister


def sign_up_by_html(request):
    users = ['Anton', 'Vitek', 'Sofiy', 'Hasan']
    info = {}

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            return HttpResponse(f'Приветствуем, {username}!')

        print(f"Имя: {username}")
        print(f"Пароль: {password}")
        print(f"Повтор пароля: {repeat_password}")
        print(f"Возраст: {age}")


    return render(request, 'registration_page.html', info)


def sign_up_by_django(request):
    users = ['Anton', 'Vitek', 'Sofiy', 'Hasan']
    info = {}
    form = UserRegister()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            else:
                return HttpResponse(f'Приветствуем, {username}!')

    info['form'] = form
    return render(request, 'registration_page.html', info)

def main_page(request):
    return HttpResponse("Это главная страница")