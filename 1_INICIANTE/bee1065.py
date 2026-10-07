num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())

even_vals = 0
nums_list = [num_1, num_2, num_3, num_4, num_5]
for val in nums_list:
    if val%2==0:
        even_vals+=1
        
print(f"{even_vals} valores pares")
