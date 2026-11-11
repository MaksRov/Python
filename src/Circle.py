# Импорт всего необходимого

from src.Figure import Figure
from math import pi
from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square

# Создание класса фигуры Круг

class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Радиус круга должен быть больше нуля.')
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Передана неизвестная фигура')
        return self.area() + figure.area()

c = Circle(5)
c.area()
c.perimeter()