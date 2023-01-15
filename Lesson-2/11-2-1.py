# Задача 1. Машина
#
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.
#

class Toyota:
    color = 'red'
    coast = 1000000
    max_speed = 200
    current_speed = 0


import random

auto1 = Toyota()
auto2 = Toyota()
auto3 = Toyota()

auto1.current_speed = random.randint(0, 200)
auto2.current_speed = random.randint(0, 200)
auto3.current_speed = random.randint(0, 200)

print("Текущие скорости наших авто:", auto1.current_speed, auto2.current_speed, auto3.current_speed)
