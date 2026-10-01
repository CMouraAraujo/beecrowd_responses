seller_name = input()
fix_salary = float(input())
total_month_value_seller = float(input())

comission_seller = total_month_value_seller * 0.15
final_salary = fix_salary + comission_seller

print(f"TOTAL = R$ {final_salary:.2f}")