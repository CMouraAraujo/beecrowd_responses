i = 0
j = 0
another_count = 0
while i <= 2.0:
    while another_count < 3:
        j+=1
        i = float(f"{i:.1f}")
        j = float(f"{j:.1f}")
        i = int(i) if i%1==0 else float(f"{i:.1f}")
        j = int(j) if j%1==0 else float(f"{j:.1f}")
        print(f"I={i} J={j}")
        another_count+=1
    i+=0.2
    j-=3
    j+=0.2
    another_count=0