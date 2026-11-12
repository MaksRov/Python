import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize("cond, exp", [
    ((1, 1), 1),
    ((1, 10), 10),
    ((2.5, 4.5), 11.25),
    ((2, 6.3), 12.6)
])
def test_area_positive(cond, exp):
    s = Rectangle(cond[0], cond[1])
    assert s.area() == exp


@pytest.mark.parametrize("cond, exp", [
    ((1, 1), 4),
    ((1, 10), 22),
    ((2.5, 4.5), 14.0),
    ((2, 6.3), 16.6)
])
def test_perimeter_positive(cond, exp):
    r = Rectangle(cond[0], cond[1])
    assert r.perimeter() == exp


@pytest.mark.parametrize("cond", [
    (-0.04, 1),
    (4, -5),
    (0, 0),
    (0, 4),
    (3.21, 0),
    (-1, -1),
    (2, -3.1)
])
def test_value_error(cond):
    with pytest.raises(ValueError):
        Rectangle(cond[0], cond[1])


def test_name():
    r = Rectangle(5, 12)
    assert r.name == 'Прямоугольник'


@pytest.mark.parametrize("cond", [("вап"), ("rtg"), ("!?"), (None)])
def test_type_error(cond):
    with pytest.raises(TypeError):
        Rectangle(cond)


def test_add_area_circle(basic_rectangle):
    sum = basic_rectangle.add_area(Circle(3))
    assert sum != 0


def test_add_area_triangle(basic_rectangle):
    sum = basic_rectangle.add_area(Triangle(3, 4, 5))
    assert sum != 0


def test_add_area_square(basic_rectangle):
    sum = basic_rectangle.add_area(Square(5))
    assert sum != 0


def test_broken_add_area():
    r = Rectangle(2, 5)
    with pytest.raises(ValueError):
        r.add_area(123)
