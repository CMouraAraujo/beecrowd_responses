entry_value = int(input())
finish_value = int(input())
sum_odd = 0

for n in range(finish_value+1, entry_value):
    if n%2==0:
        pass
    else:
        sum_odd+=n
        
print(sum_odd)
