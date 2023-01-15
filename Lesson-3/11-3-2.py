# Задача 2. Семья
#
# Реализуйте класс «Семья», который состоит из атрибутов «funds»,
# Деньги» и «Наличие дома» и объекты которого могут выполнять следующие действия:
#
# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»).
# Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.
#
#
#
# Пример работы программы (вывод информации, покупка дома, заработок, очередная покупка):
# Family name: Common family
# Family funds: 100000
# Having a house: False

# Try to buy a house
#
# Not enough money!
#
# Earned 800000 money! Current value: 900000
#
# Try to buy a house again
#
# House purchased! Current money: 0.0

#
# Family name: Common family
# Family funds: 0.0
# Having a house: True

class family:
    name = 'Common family'
    funds = 0.0
    house = False

    def info(self):
        print('Фамилия: {}\nДеньги в наличии: {}\nНаличие дома: {}\n'.format(
            self.name, self.funds, self.house
        ))

    def earnings(self, money):
        self.funds += money
        print('Вы накопили:', self.funds)

    def buy_house(self, coast, discount=0):
        coast -= coast * discount / 100
        if self.funds >= coast:
            self.funds -= coast
            print('Поздравляю, вы купили дом! Остаток средств:', self.funds)
        else:
            print('Увы, у вас недостаточно средств для покупки дома')


family1 = family()
family1.info()

print('Хотим купить дом')
family1.buy_house(8000000)

print('У семьи появились денежки')
family1.earnings(10000000)

print('Еще попытка купить дом')
family1.buy_house(8000000, 10)

