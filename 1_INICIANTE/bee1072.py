total_loop = int(input())
n_in = 0
n_out = 0

for n in range(total_loop):
    new_val = int(input())
    if 10 <= new_val <= 20:
        n_in+=1
    else:
        n_out+=1
        
print(f"{n_in} in")
print(f"{n_out} out")
