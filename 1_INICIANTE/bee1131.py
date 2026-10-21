vitorias_inter = 0
vitorias_gremio = 0
soma_grenais = 0
empates = 0
while True:
    soma_grenais+=1
    gols_inter, gols_gremio = map(int, input().split())
    if gols_inter > gols_gremio:
        vitorias_inter+=1
    elif gols_inter < gols_gremio:
        vitorias_gremio+=1
    else:
        empates+=1
    
    print("Novo grenal (1-sim 2-nao)")
    grenal = int(input())
    if grenal == 1:
        pass
    else:
        break
print(f"{soma_grenais} grenais")
print(f"Inter:{vitorias_inter}")
print(f"Gremio:{vitorias_gremio}")
print(f"Empates:{empates}")

if vitorias_inter > vitorias_gremio:
    vencedor = "Inter venceu mais"
elif vitorias_inter < vitorias_gremio:
    vencedor = "Gremio venceu mais"
else:
    vencedor = "Nao houve vencedor"
    
print(vencedor)
