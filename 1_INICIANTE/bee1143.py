import math

qtd_loops = int(input())

for n in range(1, qtd_loops+1):
    print(int(math.pow(n, 1)), end=" ")
    print(int(math.pow(n, 2)), end=" ")
    print(int(math.pow(n, 3)))
