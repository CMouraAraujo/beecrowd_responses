quantity = int(input())
list_mean = []

def pond_mean(val1, val2, val3):
    mean = ((val1*2)+(val2*3)+(val3*5)) / 10
    return f"{mean:.1f}"


for _ in range(quantity):
    val_one, val_two, val_three = map(float, input().split())
    result_mean = pond_mean(val_one, val_two, val_three)
    list_mean.append(result_mean)
    
for n in list_mean:
    print(n)
