num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())

even_vals = 0
odd_vals = 0
pos_vals= 0
neg_vals = 0

nums_list = [num_1, num_2, num_3, num_4, num_5]
for val in nums_list:
    if val%2==0:
        even_vals+=1
    if val>0:
        pos_vals+=1
    if val<0:
        neg_vals+=1
    if val%2!=0:
        odd_vals+=1

        
print(f"{even_vals} valor(es) par(es)")
print(f"{odd_vals} valor(es) impar(es)")
print(f"{pos_vals} valor(es) positivo(s)")
print(f"{neg_vals} valor(es) negativo(s)")
