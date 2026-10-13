total_values = []

for n in range(100):
    value = int(input())
    if value > 0:
        total_values.append(value)

max_value = max(total_values)
index_max_value = total_values.index(max_value)

print(max_value)
print(index_max_value+1)