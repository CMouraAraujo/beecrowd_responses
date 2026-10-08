value_loop = int(input())

for n in range (1, value_loop+1):
    if n%2==0:
        double_n = n**2
        print(f"{n}^2 = {double_n}")