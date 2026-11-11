# Импорт всего необходимого

from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Triangle import Triangle


class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть больше 0")
        super().__init__(side, side)


a = Square(45)
print(a.area(), a.perimeter())
