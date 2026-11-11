# Импорт всего необходимого

from src.Rectangle import Rectangle


class Square(Rectangle):
    name = 'Квадрат'
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Сторона квадрата должна быть больше 0")
        super().__init__(side, side)
