notas = []
exibir_media = True

while True:
    while len(notas) < 2:
        nota = float(input())
        if nota < 0 or nota > 10:
            print("nota invalida")
        else:
            notas.append(nota)
            
    if exibir_media:    
        print(f"media = {(sum(notas)/2):.2f}")
        exibir_media = False
    
    print("novo calculo (1-sim 2-nao)")
    escolha = int(input())
    if escolha == 1:
        notas = []
        exibir_media = True
    elif escolha == 2:
        break
    else:
        pass