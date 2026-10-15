i = 1
j = 7
another_count = 0

while j < 16:
    while another_count != 3:
        print(f"I={i} J={j}")
        j-=1
        another_count+=1
    i+=2
    j+=5
    another_count=0