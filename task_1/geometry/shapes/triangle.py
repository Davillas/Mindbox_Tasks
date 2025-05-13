from math import sqrt
from task_1.geometry.shapes.shape import Shape
from task_1.services.validators import is_right_triangle, is_valid_triangle

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if not is_valid_triangle(a, b, c):
            raise ValueError("Triangle cannot be created with provided sides!")
        self.a, self.b, self.c = a, b, c
    
    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def is_right(self) -> bool:
        return is_right_triangle(self.a, self.b, self.c)