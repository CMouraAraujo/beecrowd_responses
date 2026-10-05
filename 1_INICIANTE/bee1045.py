import math

point_a, point_b, point_c = map(float, input().split())
helper_variable = None

if point_a >= point_b:
    if point_b >= point_c:
        pass # a, b, c
    elif point_c >= point_b:
        if point_c >= point_a:  # c, a, b
            helper_variable = point_b
            point_b = point_a
            point_a = point_c
            point_c = helper_variable  # Sei muito bem que com lista resolveria rapidamente usando Sort, mas eu quis inventar um pouco
        else: # a, c, b
            helper_variable = point_b
            point_b = point_c
            point_c = helper_variable
elif point_b >= point_a: 
    if point_a >= point_c: # b, a, c
        helper_variable = point_a
        point_a = point_b
        point_b = helper_variable
    elif  point_c >= point_a: #b, c, a
        if point_b >= point_c:
            helper_variable = point_a
            point_a = point_b
            point_b = point_c
            point_c = helper_variable
        else: # c, b, a
            helper_variable = point_c
            point_c = point_a
            point_a = helper_variable
        

if point_a >= point_b + point_c:
    print("NAO FORMA TRIANGULO")
else:
    if math.pow(point_a, 2) == math.pow(point_b, 2) + math.pow(point_c, 2):
        print("TRIANGULO RETANGULO")
    if math.pow(point_a, 2) > math.pow(point_b, 2) + math.pow(point_c, 2):
        print("TRIANGULO OBTUSANGULO")
    if math.pow(point_a, 2) < math.pow(point_b, 2) + math.pow(point_c, 2):
        print("TRIANGULO ACUTANGULO")
    if point_a == point_b == point_c:
        print("TRIANGULO EQUILATERO")
    if (point_a == point_b and point_b != point_c):
        print("TRIANGULO ISOSCELES")
    if (point_a == point_c and point_a != point_b):
        print("TRIANGULO ISOSCELES")
    if (point_c ==  point_b and point_c != point_a):
        print("TRIANGULO ISOSCELES")
