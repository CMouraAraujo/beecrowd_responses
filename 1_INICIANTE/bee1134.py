alcool = gasolina = diesel = 0

while True:
    tipo_gasolina = int(input())
    match tipo_gasolina:
        case 1:
            alcool+=1
        case 2:
            gasolina+=1
        case 3:
            diesel+=1
        case 4:
            break
        case _:
            pass

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}")