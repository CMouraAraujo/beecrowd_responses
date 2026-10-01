import math

a, b, c = map(float, input().split())

delta = math.pow(b, 2) - (4 * a * c)

if a==0 or delta<0:
    print("Impossivel calcular")  
else:
    bhaskar_positive = (-b + math.sqrt(delta)) / (2 * a)
    bhaskara_negative = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {bhaskar_positive:.5f}")
    print(f"R2 = {bhaskara_negative:.5f}")
