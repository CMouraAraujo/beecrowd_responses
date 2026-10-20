quant_divisao = int(input())
for _ in range(quant_divisao):
    val1, val2 = map(int, input().split())
    try:
        result = val1/val2
        print(f"{result:.1f}")
    except ZeroDivisionError:
        print("divisao impossivel")