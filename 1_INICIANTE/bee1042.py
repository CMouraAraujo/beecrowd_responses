values = list(map(int, input().split()))
values_sorted = sorted(values)
for val in values_sorted:
    print(val)
    
print()

for val in values:
    print(val)


# first_val, sec_val, third_val = map(int, input().split())

# if  first_val < sec_val:
#     if first_val < third_val:
#         print(first_val)
#         if third_val < sec_val:
#             print(third_val)
#             print(sec_val)
#         else:
#             print(sec_val)
#             print(third_val)
#     else:
#         print(third_val)
#         print(first_val)
#         print(sec_val)
# elif sec_val < third_val:
#     print(sec_val)
#     if third_val < first_val:
#         print(third_val)
#         print(first_val)
#     else:
#         print(first_val)
#         print(third_val)
# else:
#     print(third_val)
#     print(sec_val)
#     print(first_val)
    
        