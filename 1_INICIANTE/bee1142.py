init = 1
end = 5
qtd_loops = int(input())

for val in range(qtd_loops):
    for n in range(init, end):
        if n%4!=0:
            print(n, end=" ")
        else:
            print("PUM")
    init+=4
    end+=4