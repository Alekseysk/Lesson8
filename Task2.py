"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых
пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.
"""


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt
        

dividend, divisor = input("Введите делимое и делитель через пробел: ").strip().split()

try:
    dividend = int(dividend)
    divisor = int(divisor)
    if divisor == 0:
        raise MyException("Деление на ноль!!!")
except ValueError:
    print("Вы ввели не число")
except MyException as err:
    print(err)
else:
    print(f"Все хорошо. результат: {dividend / divisor}")
