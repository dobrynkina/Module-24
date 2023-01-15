# Задача 1. Машина 2
#
# Модернизируйте класс Toyota из прошлого видео. Атрибуты остаются такими же:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
#
#
# Добавьте два метода класса:
#
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.

class Toyota:
    color = 'red'
    coast = 1000000
    max_speed = 200
    current_speed = 0

    def info(self):
        print("цвет: {}\nстоимость: {}\nмаксимальная скорость: {}\nтекущая скорость: {}".format(
            self.color, self.current_speed, self.max_speed, self.current_speed))

    def new_speed(self, new_speed):
        self.current_speed = new_speed


auto1 = Toyota()
auto1.new_speed(100)
auto1.info()
