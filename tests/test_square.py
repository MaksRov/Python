import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize("cond, exp", [
    (1, 1),
    (5, 25),
    (2.5, 6.25)
])
def test_area_positive(cond, exp):
    s = Square(cond)
    assert s.area() == exp


@pytest.mark.parametrize("cond, exp", [
    (1, 4),
    (5, 20),
    (2.5, 10)
])
def test_perimeter_positive(cond, exp):
    s = Square(cond)
    assert s.perimeter() == exp


@pytest.mark.parametrize("cond", [(-0.04), (0), (-45)])
def test_value_error(cond):
    with pytest.raises(ValueError):
        Square(cond)


def test_name(basic_square):
    assert basic_square.name == 'Квадрат'


@pytest.mark.parametrize("cond", [("вап"), ("rtg"), ("!?"), (None)])
def test_type_error(cond):
    with pytest.raises(TypeError):
        Square(cond)


def test_add_area_circle(basic_square):
    sum = basic_square.add_area(Circle(3))
    assert sum != 0


def test_add_area_triangle(basic_square):
    sum = basic_square.add_area(Triangle(3, 4, 5))
    assert sum != 0


def test_add_area_rectangle(basic_square):
    sum = basic_square.add_area(Rectangle(3, 4))
    assert sum != 0


def test_broken_add_area(basic_square):
    with pytest.raises(ValueError):
        basic_square.add_area(123)
