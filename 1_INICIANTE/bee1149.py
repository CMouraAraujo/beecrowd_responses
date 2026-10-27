numbers = list(map(int, input().split()))
valores = []
valor = 0

for n in numbers[1:]:
    if n > 0:
        valor = n
        
for i in range(valor):
    valores.append(numbers[0]+i)

print(sum(valores))