"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Data:
    day: int = 1
    month: int = 1
    year: int = 1
    date: str = '1'
    
    def __init__(self, date):
        self.date = date
    
    def __str__(self):
        return f'Указана дата {self.day}/{self.month}/{self.year}'
    
    @classmethod
    def extract(cls, date):
        cls.day, cls.month, cls.year = cls.check(date)
    
    @staticmethod
    def check(date):
        day, month, year = [int(val) for val in date.split('-')]
        if (0 < day < 32) and (0 < month < 13) and (year > 0):
            return day, month, year
        else:
            return None, None, None


my_date = Data('23-12-1976')
my_date.extract('23-12-1976')
print(my_date)

my_date.extract('31-6-1995')
print(my_date)