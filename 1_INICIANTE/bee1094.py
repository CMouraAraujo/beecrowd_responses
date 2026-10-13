coelhos = 0
ratos = 0
sapos = 0
total = 0

loop = int(input())

for n in range(loop):
    value = input().split(" ")
    total+=int(value[0])
    
    if value[1] == "C":
        coelhos+=int(value[0])
    elif value[1] == "R":
        ratos+=int(value[0])
    elif value[1] == "S":
        sapos+=int(value[0])

total_coelhos = (coelhos/total)*100   
total_ratos = (ratos/total)*100   
total_sapos = (sapos/total)*100   

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {total_coelhos:.2f} %")
print(f"Percentual de ratos: {total_ratos:.2f} %")
print(f"Percentual de sapos: {total_sapos:.2f} %")
