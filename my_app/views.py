from django.shortcuts import render

from django.http import HttpResponse

"""
Настройте работу сервера в вашей локальной сети.
📌 Убедитесь что при запуске на ПК, сайт можно посмотреть в
браузере другого устройства локальной сети: другой ПК,
ноутбук, телефон и т.п.
Создайте представление “Привет, мир!” внутри вашего
первого приложения.
📌 Настройте маршруты
"""


def index(request):
    return HttpResponse("Привет, мир!")