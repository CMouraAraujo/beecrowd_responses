qtd_in_line, loops = map(int, input().split())
count=1

while True:
    for number in range(1, loops+1):
        if count != qtd_in_line:
            end_print = " "
            count+=1
        else:
            end_print = "\n"
            count=1
        print(number, end=end_print)
    break