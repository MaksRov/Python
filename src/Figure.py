# Создание базового класса геометрической фигуры

class Figure:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError('Вычисление площади фигуры не реализовано в наследнике')

    def perimeter(self):
        raise NotImplementedError('Вычисление периметра фигуры не реализовано в наследнике')
