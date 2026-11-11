# Импорт всего необходимого

from src.Figure import Figure


# Создание класса фигуры Прямоугольник

class Rectangle(Figure):
    name = 'Прямоугольник'
    def __init__(self, first_side, second_side):
        if first_side <= 0 or second_side <= 0:
            raise ValueError("Стороны прямоугольника должны быть больше 0")
        self.first_side = first_side
        self.second_side = second_side

    def area(self):
        return self.first_side * self.second_side

    def perimeter(self):
        return (self.first_side + self.second_side) * 2

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError('Передана неизвестная фигура')
        return self.area() + figure.area()
