import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
from math import pi


@pytest.mark.parametrize("cond, exp", [
    (1, pi * 1 ** 2),
    (5, pi * 5 ** 2),
    (2.5, pi * 2.5 ** 2)
])
def test_area_positive(cond, exp):
    s = Circle(cond)
    assert s.area() == exp


@pytest.mark.parametrize("cond, exp", [
    (1, pi * 1 * 2),
    (5, pi * 5 * 2),
    (2.5, pi * 2.5 * 2)
])
def test_perimeter_positive(cond, exp):
    s = Circle(cond)
    assert s.perimeter() == exp


@pytest.mark.parametrize("cond", [(-0.04), (0), (-45)])
def test_value_error(cond):
    with pytest.raises(ValueError):
        Circle(cond)


def test_name(basic_circle):
    assert basic_circle.name == 'Круг'


@pytest.mark.parametrize("cond", [("вап"), ("rtg"), ("!?"), (None)])
def test_type_error(cond):
    with pytest.raises(TypeError):
        Circle(cond)


def test_add_area_circle(basic_circle):
    sum = basic_circle.add_area(Square(3))
    assert sum != 0


def test_add_area_triangle(basic_circle):
    sum = basic_circle.add_area(Triangle(3, 4, 5))
    assert sum != 0


def test_add_area_rectangle(basic_circle):
    sum = basic_circle.add_area(Rectangle(3, 4))
    assert sum != 0


def test_broken_add_area(basic_circle):
    with pytest.raises(ValueError):
        basic_circle.add_area(123)
