number = int(input())

if 1 <= number <= 1000:
    for n in range(number+1):
        if n%2!=0:
            print(n)