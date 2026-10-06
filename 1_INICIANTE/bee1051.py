value = float(input())
total_tax = 0
if value <= 2000:
    print("Isento")
else:
    if value > 4500:
        tribute_value = value - 4500
        total_tax += tribute_value * 0.28
        value = 4500
        
    if 3000 < value <= 4500:
        tribute_value = value - 3000
        total_tax += tribute_value * 0.18
        value = 3000

    if 2000 < value <= 3000:
        tribute_value = value - 2000
        total_tax += tribute_value * 0.08
        value = 2000

    if value <= 2000:
        pass

    print(f"R$ {total_tax:.2f}")