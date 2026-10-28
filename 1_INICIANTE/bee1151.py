valor = int(input())
numero_inicial = 0
numero_anterior = 0
assistente = 1

if valor < 46 and valor > 0:
    for _ in range(valor):
        end = "\n" if _ == valor-1 else " "
        
        print(numero_inicial, end=end)
        numero_anterior = numero_inicial
        numero_inicial = assistente
        assistente = numero_anterior + numero_inicial
        