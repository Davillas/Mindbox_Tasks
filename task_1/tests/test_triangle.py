from task_1.geometry.shapes.triangle import Triangle
import pytest

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert round(t.area(), 2) == 6.0

def test_right_triangle():
    t = Triangle(3, 4, 5)
    assert t.is_right() is True

def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)
