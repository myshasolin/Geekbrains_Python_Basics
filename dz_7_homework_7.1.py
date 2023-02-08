# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.
class UserMatrix:
    count = 0

    def __init__(self, user_numbers=None, user_line=None):
        self.user_numbers = user_numbers
        self.user_line = user_line
        UserMatrix.count += 1
        print(f'\nформируем матрицу нубмер {UserMatrix.count}\n')

    @property
    def user_matrix(self):
        user_matrix = None
        while not self.user_numbers:
            try:
                self.user_numbers = int(input('сколько цифер по горизонтали? '))
                self.user_line = int(input('a по вертикали сколько? '))
                user_matrix = [[int(input(f'{i+1} цифра строки: ')) for i in range(self.user_numbers)]
                               for i in range(self.user_line)]
            except ValueError:
                print('цифру не ввёл, давай-ка повнимательней. Начнём заново')
                self.user_numbers = None
        print('такая вот матрица получилась:\n')
        return user_matrix


class Matrix:

    def __init__(self):
        self.matrix_overload = UserMatrix().user_matrix

    @property
    def overload(self):
        for x in range(len(self.matrix_overload)):
            for y in range(len(self.matrix_overload[x])):
                print(self.matrix_overload[x][y], end=' ')
            print()
        return ''

    def __str__(self):
        return str(self.matrix_overload)

    def __add__(self, other, checking_the_size=None):
        while not checking_the_size:
            if len(self.matrix_overload) == len(other.matrix_overload):
                for v in range(len(other.matrix_overload)):
                    for w in range(len(other.matrix_overload[v])):
                        print(other.matrix_overload[v][w] + self.matrix_overload[v][w], end=' ')
                    print()
                checking_the_size = True
            else:
                print('у тебя матрицы разного рамера, дурачелло')
                self.matrix_overload = []
                other.matrix_overload = []
        return ''


a = Matrix()
print(a.overload)

print('матрица в виде списка:')
print(a)

b = Matrix()
print(b.overload)

print('матрица в виде списка:')
print(b)

print('результат сложения двух матриц:')
addition_of_two_matrices = a + b
print(addition_of_two_matrices)
