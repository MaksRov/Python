import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.parametrize("cond, exp", [(1, 1), (5, 25), (2.5, 6.25)])
def test_area_positive(cond, exp):
    s = Square(cond)
    assert s.area() == exp

@pytest.mark.parametrize("cond", [(-0.04), (0), (-45)])
def test_value_error(cond):
    with pytest.raises(ValueError):
        Square(cond)

def test_name():
    s = Square(5)
    assert s.name == 'Квадрат'

@pytest.mark.parametrize("cond", [("вап"), ("rtg"), ("!?"), (None)])
def test_type_error(cond):
    with pytest.raises(TypeError):
        Square(cond)

def test_add_area_circle():
    s = Square(5)
    sum = s.add_area(Circle(3))
    assert sum != 0

def test_add_area_triangle():
    s = Square(5)
    sum = s.add_area(Triangle(3, 4, 5))
    assert sum != 0

def test_add_area_rectangle():
    s = Square(5)
    sum = s.add_area(Rectangle(3, 4))
    assert sum != 0

def test_broken_add_area():
    s = Square(5)
    with pytest.raises(ValueError):
        s.add_area(123)