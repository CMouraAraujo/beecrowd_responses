import math

a_point, b_point, c_point = map(float, input().split())

PI = 3.14159

RECTANGLE_TRIANGLE_AREA = (a_point * c_point) / 2
CIRCLE_AREA = PI * math.pow(c_point, 2)
TRAPEZOID_AREA = ((a_point + b_point) * c_point) / 2
SQUARE_AREA = math.pow(b_point, 2)
RECTANGLE_AREA = a_point * b_point

print(f"""TRIANGULO: {RECTANGLE_TRIANGLE_AREA:.3f}
CIRCULO: {CIRCLE_AREA:.3f}
TRAPEZIO: {TRAPEZOID_AREA:.3f}
QUADRADO: {SQUARE_AREA:.3f}
RETANGULO: {RECTANGLE_AREA:.3f}""")
