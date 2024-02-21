from random import randint, choice
import logging
from django.shortcuts import render
from django.http import HttpResponse
from .forms import GamesForm

"""
Задание №5-6
📌 Создайте новое приложение. Подключите его к проекту. В
приложении должно быть три простых представления,
возвращающих HTTP ответ:
📌 Орёл или решка
📌 Значение одной из шести граней игрального кубика
📌 Случайное число от 0 до 100
📌 Пропишите маршруты
Добавьте логирование в проект.
📌 Настройте возможность вывода в файл и в терминал.
📌 Устраните возможные ошибки.
📌 *Форматирование настройте по своему желанию.
Объясните что вы выводите в логи

Доработаем задачу 7 из урока 1, где бросали монетку,
игральную кость и генерировали случайное число.
📌 Маршруты могут принимать целое число - количество
бросков.
📌 Представления создают список с результатами бросков и
передают его в контекст шаблона.
📌 Необходимо создать универсальный шаблон для вывода
результатов любого из трёх представлений.

Доработаем задачу 1.
📌 Создайте представление, которое выводит форму выбора.
📌 В зависимости от переданных значений представление
вызывает одно из трёх представлений, созданных на
прошлом семинаре (если данные прошли проверку, конечно
же).
"""

logger = logging.getLogger(__name__)


# def gen_coin(request):
#     coin = randint(0, 1)
#     if coin == 0:
#         return HttpResponse("Выпал орёл")
#     return HttpResponse("Выпала решка")
def log(func):
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        logger.info(f'The function {func.__name__} was returned: {response.content.decode()}')
        return response

    return wrapper


@log
def gen_coin(request, num):
    results = [choice(['Tail', 'Head']) for _ in range(num)]
    context = {"game_name": "бросок монеты", "results": results}
    return render(request, 'my_app2/game.html', context)


@log
def gen_dice(request, num):
    results = [randint(1, 7) for _ in range(num)]
    context = {"game_name": "бросок игральной кости", "results": results}
    return render(request, 'my_app2/game.html', context)


@log
def gen_number(request, num):
    results = [randint(0, 100) for _ in range(num)]
    context = {"game_name": "случайное число", "results": results}
    return render(request, 'my_app2/game.html', context)


def select_game(request):
    if request.method == 'POST':
        form = GamesForm(request.POST)
        if form.is_valid():
            action = form.cleaned_data.get('action')
            quantity = form.cleaned_data.get('quantity')
            if action == 'Coin':
                return gen_coin(request, quantity)
            if action == 'Dice':
                return gen_dice(request, quantity)
            if action == 'Number':
                return gen_number(request, quantity)
    else:
        form = GamesForm()
    return render(request, 'my_app2/games.html', {'form': form})
