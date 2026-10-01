a, b, c = map(int, input().split())

two_values_comparation = (a+b+abs(a-b)) / 2
three_values_comparation = ((two_values_comparation) + c + abs((two_values_comparation) - c)) / 2

print(f"{int(three_values_comparation)} eh o maior")