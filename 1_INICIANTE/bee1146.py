while True:
    val = int(input())
    if val==0:
        break
    else:
        for i in range(1, val+1):
            if i==val:
                end="\n"
            else:
                end=" "
            print(i, end=end)