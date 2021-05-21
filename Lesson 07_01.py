"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

import random
import itertools

class Matrix:
    def __init__(self, matrix_list: list):
        self.matrix_list = matrix_list

    def __str__(self):
        str_matrix = ""
        for i in self.matrix_list:
            for j in i:
                str_matrix += str(j) + " "*(3-len(str(j)))
            str_matrix += '\n'
        return str_matrix

    def __add__(self, other):
        if len(self.matrix_list) == len(other.matrix_list) and len(self.matrix_list[0]) == len(other.matrix_list[0]):
            add_matrix = []
            for i in range(len(self.matrix_list)):
                add_matrix1 = []
                for j, k in zip(self.matrix_list[i], other.matrix_list[i]):
                    add_matrix1.append(j+k)
                add_matrix.append(add_matrix1)
            return Matrix(add_matrix).__str__()
        else:
            return f"Матрицы должны быть одинакового размера"

def matrix_gen():
    new_list = []
    for i in range(0, 5):
        new_list_2 = []
        for e in range(0, 6):
            new_list_2.append(random.randint(1, 30))
        new_list.append(new_list_2)
    return new_list


neo = Matrix(matrix_gen())
print(neo)
trinity = Matrix(matrix_gen())
print(trinity)

print(neo+trinity)





