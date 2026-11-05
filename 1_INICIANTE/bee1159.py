soma=0
resultados = []
while True:
    val = int(input())
    if val>0 or val<0:
        soma=0
        for _ in range(5):
            if val%2==0:
                soma+=val
                val+=2
            else:
                val+=1
                soma+=val
                val+=2
        resultados.append(soma)
    else:
        break
    
for resultado in resultados:
    print(resultado)