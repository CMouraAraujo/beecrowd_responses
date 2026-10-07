num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())
num_6 = float(input())

positive_values = []
nums_list = [num_1, num_2, num_3, num_4, num_5, num_6]
positive_values = [num for num in nums_list if num>0]

sum_num = sum(positive_values)
mean = sum_num / len(positive_values)

print(f"{len(positive_values)} valores positivos")
print(f"{mean:.1f}")
