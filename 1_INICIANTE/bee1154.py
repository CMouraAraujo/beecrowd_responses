import statistics

idades = []
while True:
    idade = int(input())
    if idade < 0:
        break
    idades.append(idade)

media_idades = statistics.mean(idades)
print(f"{media_idades:.2f}")