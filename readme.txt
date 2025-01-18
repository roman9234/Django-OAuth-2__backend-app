python manage.py createsuperuser
admin
admin@mail.ru
qwerty

Использование административной панели:
http://127.0.0.1:8000/admin/
Аутентифицируемся


Настраиваем библиотеку
social-auth-app-django

Добавляем в INSTALLED APPS:
'social_django',

Указываем в секции Templates шаблоны для context_processors:
    'social_django.context_processors.backends',
    'social_django.context_processors.login_redirect',


Для работы библиотеки надо внести данные в секцию
Будем использовать ВК

AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

Добавляем переменные ккоторые будут отвечать за учётные данные
Эти данные надо почитать документацию
Создаём приложение в вк для разработчиков
тип сайт
в адресе тип http localhost 8000
Базовый домен hocalhost
Проходим аутентификацию
Берём в настройках приложения ID приложения
Там же берём защищённый ключ
далее OAUTH_VK_CKOPE - список передаваемых данных и разрешений (работа оффлайн)


SOCIAL_AUTH_VK_OAUTH2_KEY = '51670653'
...


Далее надо указать маршруты чтобы могло работать.
Для этого в приложении создаём файл urls.pyв oaauth_app
В urlpatterns добавляем нужные пути
TODO описать какие пути и что с другим urls проекта а не прилоежния






