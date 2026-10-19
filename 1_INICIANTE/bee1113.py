list_results = []
while True:
    num_one, num_two = map(int, input().split())
    
    if num_one == num_two:
        break
    elif num_one > num_two:
        list_results.append("Decrescente")
    elif num_one < num_two:
        list_results.append("Crescente")
        
for val in list_results:
    print(val)