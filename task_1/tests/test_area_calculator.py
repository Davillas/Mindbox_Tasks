from task_1.geometry.shapes.circle import Circle
from task_1.geometry.shapes.triangle import Triangle
from task_1.geometry.area_calculator import calculate_area

def test_compute_area_circle():
    assert calculate_area(Circle(1)) > 0

def test_compute_area_triangle():
    assert calculate_area(Triangle(3, 4, 5)) == 6.0