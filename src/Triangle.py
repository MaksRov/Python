# Импортируем базовый класс фигуры
from src.Figure import Figure
from math import sqrt


# Создаем класс треугольника

class Triangle(Figure):
    name = 'Треугольник'
    def __init__(self, first_side, second_side, third_side):
        if first_side <= 0 or second_side <= 0 or third_side <= 0:
            raise ValueError('Стороны треугольника должны быть > 0')
        if first_side + second_side <= third_side or first_side + third_side <= second_side or second_side + third_side <= first_side:
            raise ValueError('Треугольник с заданными сторонами не может существовать')
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    # Вычисление площади фигуры

    def area(self):
        p = (self.first_side + self.second_side + self.third_side) / 2
        return sqrt(p * (p - self.first_side) * (p - self.second_side) * (p - self.third_side))

    # Вычисление периметра фигуры

    def perimeter(self):
        return self.first_side + self.second_side + self.third_side

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Передана неизвестная фигура')
        return self.area() + figure.area()


# print('Для вычисления площади и периметра треугольника введите его стороны:')
# a = Triangle(int(input()), int(input()), int(input()))
# print('Площадь треугольника:', a.area())
# print('Периметр треугольника:', a.perimeter())
