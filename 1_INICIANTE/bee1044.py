first_val, secnd_val = map(int, input().split())

if first_val % secnd_val == 0 or secnd_val % first_val == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")