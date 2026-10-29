fatorial = int(input())
resultado = 1
for val in range(fatorial, 0, -1):
    resultado*=val
print(resultado)