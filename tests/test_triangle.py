import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize("cond, exp", [
    ((13, 14, 15), 84)
])
def test_area_positive(cond, exp):
    t = Triangle(cond[0], cond[1], cond[2])
    assert t.area() == exp


@pytest.mark.parametrize("cond, exp", [
    ((1, 1, 1), 3),
    ((3, 4, 5), 12)
])
def test_perimeter_positive(cond, exp):
    t = Triangle(cond[0], cond[1], cond[2])
    assert t.perimeter() == exp


@pytest.mark.parametrize("cond", [
    (-0.04, 1, 2),
    (4, -5, 1),
    (0, 0, 0),
    (-1, -1, -1)
])
def test_value_error(cond):
    with pytest.raises(ValueError):
        Triangle(cond[0], cond[1], cond[2])


def test_name(basic_triangle):
    assert basic_triangle.name == 'Треугольник'


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