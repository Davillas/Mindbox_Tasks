from task_1.geometry.shapes.shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be non-negative!")
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius * self.radius