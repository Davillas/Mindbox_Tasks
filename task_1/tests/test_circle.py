from task_1.geometry.shapes.circle import Circle
import pytest
from math import pi

def test_circle_area():
    c = Circle(1)
    assert round(c.area(), 5) == round(pi, 5)

def test_circle_invalid_radius():
    with pytest.raises(ValueError):
        Circle(0)

def test_circle_negative_radius():
    with pytest.raises(ValueError):
        Circle(-1)