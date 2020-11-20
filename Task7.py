"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im
        
    def __mul__(self, other):
        return ComplexNumber((self.re * other.re - self.im * other.im), (self.re * other.im + self.im * other.re))
    
    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)
    
    def __str__(self):
        return f're {self.re} im {self.im}'
        
        
complex_number_1 = ComplexNumber(5, 2)
complex_number_2 = ComplexNumber(2, 7)
print(f'Первое комплексное число - {complex_number_1}')
print(f'Второе комплексное число - {complex_number_2}')
print(f'Сумма комплексных чисел - {complex_number_1 + complex_number_2}')
print(f'Произведение комплексных - {complex_number_1 * complex_number_2}')
