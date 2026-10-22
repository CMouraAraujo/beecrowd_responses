val1 = int(input())
val2 = int(input())

if val1 > val2:
    assistente = val1
    val1 = val2
    val2 = assistente

for n in range(val1+1, val2):
    if n%5==2 or n%5==3:
        print(n)
    