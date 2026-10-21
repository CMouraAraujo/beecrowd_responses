notas = []

while len(notas) < 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        notas.append(nota)
    
print(f"media = {(sum(notas)/2):.2f}")