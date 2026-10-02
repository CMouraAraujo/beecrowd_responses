number_one, number_two, number_tree, number_four = map(float, input().split())

def meanse(meanse_value):
    if meanse_value >= 7:
        status = "Aluno aprovado."
    elif meanse_value < 5:
        status = "Aluno reprovado."
    else:
        status = "Aluno em exame."
    return status

number_one *= 2
number_two *= 3
number_tree *= 4
status = ''
meanse_value = (number_one + number_two + number_tree + number_four) / 10
status = meanse(meanse_value)


if status == "Aluno em exame.":
    rec = float(input(""))
    new_meanse_value = (float(meanse_value) + rec) / 2
    if new_meanse_value >= 5:
        status_rec = ("Aluno aprovado.")
    else:
        status_rec = ("Aluno reprovado.")
    
    
print(f"Media: {meanse_value:.1f}")
print(status)
if status == "Aluno em exame.":
    print(f"Nota do exame: {rec:.1f}")
    print(status_rec)
    print(f"Media final: {new_meanse_value:.1f}")
    