from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# функция index которая принимает запрос от браузера и возвращает отрендеренную страницу index.html
def index(request):
    return render(request, 'index.html')


# Функция profile() отвечает за вывод профиля пользователя.
# Декоратор @login_required позволяет функции работать только у авторизованного пользователя

@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})
