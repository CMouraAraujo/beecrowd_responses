value = int(input())
sum = 0
list_of_lists = []
list_of_sums = []
for _ in range(value):
    list_vals = [int(val) for val in input().split()]
    list_vals.sort()
    list_of_lists.append(list_vals)
    
for i in range(len(list_of_lists)):    
    for val in range(list_of_lists[i][0]+1, list_of_lists[i][1]):
        if val%2!=0:
            sum+=val
    list_of_sums.append(sum)
    sum=0
        
for val in list_of_sums:
    print(val)