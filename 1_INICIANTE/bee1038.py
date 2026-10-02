product_cachorro_quente = 4.00
product_x_salada = 4.50
product_x_bacon = 5.00
product_torrada_simples = 2.00
product_refrigerante = 1.50
total_value = 0
iten, qntt = map(int, input().split())

match iten:
    case 1:
        total_value = product_cachorro_quente * qntt
    case 2:
        total_value = product_x_salada * qntt
    case 3:
        total_value = product_x_bacon * qntt
    case 4:
        total_value = product_torrada_simples * qntt
    case 5:
            total_value = product_refrigerante * qntt
print(f"Total: R$ {total_value:.2f}")
