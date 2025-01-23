from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Базовый путь редиректит на функцию index во views.py
    path('accounts/profile/', views.profile, name='profile'), # путь до аккаунта, где отображается информация от авторизованного пользователя
    path('social/', include('social_django.urls', namespace='social_auth')), # Для библиотеки нужен роут который будет называться social который будет включать в работу приложение soccial_django
]


