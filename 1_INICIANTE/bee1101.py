while True:
    sum = 0
    
    val1, val2 = map(int, input().split())
    list_vals = [val1, val2]
    list_vals.sort()
    
    if val1<=0 or val2<=0:
        break
    
    for n in range(list_vals[0], list_vals[1]+1):
        sum+=n
        print(n, end=" ")
        
    
    print(f"Sum={sum}")