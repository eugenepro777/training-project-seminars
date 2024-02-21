from random import choice
from django.db import models


"""
Создайте модель для запоминания бросков монеты: орёл или решка. 
Также запоминайте время броска
Добавьте статический метод для статистики по n последним броскам монеты. 
Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.
"""


class Side(models.Model):
    NAMES = ['Tail', 'Head']
    coin_side = models.CharField(max_length=4, default=choice(NAMES))
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Сторона монеты {self.coin_side}'

    @staticmethod
    def last_throws(n=None):
        if n is None:
            n = 0
        sides = Side.objects.all()[-n:]
        heads_count = tails_count = 0
        # head_count = sum(s.coin_side == 'Head' for s in sides)
        # tail_count = n - head_count
        for side in sides:
            if side.coin_side == 'Tail':
                tails_count += 1
            else:
                heads_count += 1

        return {"tail": tails_count, "head": heads_count}


