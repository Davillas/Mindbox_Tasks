import pytest
from geometry.shapes.triangle import Triangle
from geometry.shapes.circle import Circle

def test_triangle_with_non_numeric():
    with pytest.raises(TypeError):
        Triangle("a", 4, 5)

def test_circle_with_string():
    with pytest.raises(TypeError):
        Circle("ab")