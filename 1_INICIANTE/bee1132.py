inicio = int(input())
fim = int(input())
soma = 0

if inicio > fim:
    assistente = fim
    fim = inicio
    inicio = assistente
    
for n in range(inicio, fim+1):
    if n%13!=0:
        soma+=n

print(soma)
        