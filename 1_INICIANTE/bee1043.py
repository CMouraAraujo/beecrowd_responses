values = list(map(float, input().split()))

ordened_values = sorted(values)

if ordened_values[0] + ordened_values[1] > ordened_values[2]:
    perimeter = sum(values)
    print(f"Perimetro = {perimeter:.1f}")
else:
    area = ((values[0] + values[1]) * values[2]) / 2
    print(f"Area = {area:.1f}")