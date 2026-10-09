value = int(input())

if value < 10000:
    for n in range(1, 10000):
        if n%13==2:
            print(n)