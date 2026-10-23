loop_val = int(input())
first_val = 1
second_val = 1
third_val = 1
isTrue = True
sum_second = 0
for _ in range(loop_val*2):
    print(f"{first_val} {second_val} {third_val}")
    
    if isTrue:
        second_val+=1
        sum_second+=2
        third_val+=1
        isTrue=False
    else:
        first_val+=1
        second_val+=sum_second
        third_val=second_val*first_val
        isTrue=True
    