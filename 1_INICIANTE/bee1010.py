c_p1, n_p1, v_p1 = input().split()
c_p1 = int(c_p1)
n_p1 = int(n_p1)
v_p1 = float(v_p1)

c_p2, n_p2, v_p2 = input().split()
c_p2 = int(c_p2)
n_p2 = int(n_p2)
v_p2 = float(v_p2)

total_value = (n_p1*v_p1) + (n_p2*v_p2)
print(f"VALOR A PAGAR: R$ {total_value:.2f}")