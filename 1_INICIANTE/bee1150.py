valor_inicial = int(input())
provavel_valor_final = int(input())
soma_ate_passar_final = []

while True:
    if provavel_valor_final <= valor_inicial:
        provavel_valor_final = int(input())
    else:
        valor_final = provavel_valor_final
        break


for numero in range(valor_inicial, valor_final):
    soma_ate_passar_final.append(numero)
    if sum(soma_ate_passar_final) < valor_final:
        pass
    else:
        break
print(len(soma_ate_passar_final))