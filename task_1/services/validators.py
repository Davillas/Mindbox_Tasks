def is_valid_triangle(a: float, b: float, c: float) -> bool:
    return a + b > c and a + c > b and b + c > a

def is_right_triangle(a: float, b: float, c: float) -> bool:
    sides = sorted([a, b, c])
    return round(sides[0] ** 2 + sides[1] ** 2, 5) == round(sides[2] ** 2, 5)