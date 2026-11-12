# ФИКСТУРЫ

import pytest

from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle
from src.Triangle import Triangle


@pytest.fixture
def basic_square():
    return Square(5)

@pytest.fixture
def basic_rectangle():
    return Rectangle(2, 5)

@pytest.fixture
def basic_circle():
    return Circle(5)

@pytest.fixture
def basic_triangle():
    return Triangle(3, 4, 5)
