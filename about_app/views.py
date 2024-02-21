from django.shortcuts import render
import logging
from django.http import HttpResponse
import lorem

"""
Создайте пару представлений в вашем первом приложении:
— главная
— о себе.
Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.

Сохраняйте в логи данные о посещении страниц.
"""

logger = logging.getLogger(__name__)


# def log(func):
#     def wrapper(request, *args, **kwargs):
#         response = func(request, *args, **kwargs)
#         logger.info(f'The function {func.__name__} was returned: Посещена страница {request.path}')
#         return response
#
#     return wrapper


def index(request):
    text = lorem.paragraph()
    html = f"""<h1 align="center">Один из моих первых Django-проектов</h1>    
    <p align="center">
        <b>{text}</b>
    </p>
    <br>
    <p>
        {text * 2}
    </p>
    """
    logger.info(f'Посещена страница: {request.path}')
    return HttpResponse(html)


def about(request):
    text = lorem.paragraph()
    html = f"""<h1 align="center">Обо мне</h1>    
    <p align="center">
        {text}
    </p>    
    """
    logger.info(f'Посещена страница: {request.path}')
    return HttpResponse(html)
