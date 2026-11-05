loop = int(input())
soma=0

for _ in range(loop):
    init, quantidade = map(int, input().split())
    
    for _ in range(quantidade):
        if init%2==0:
            init+=1
            soma+=init
            init+=2
        else:
            soma+=init
            init+=2
    print(soma)
    soma = 0