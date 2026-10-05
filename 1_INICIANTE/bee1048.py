my_salary = float(input())



if 0 < my_salary <= 400:
    percent = 15
elif 400 < my_salary <= 800:
    percent = 12
elif 800 < my_salary <= 1200:
    percent = 10
elif 1200 < my_salary <= 2000:
    percent = 7
else:
    percent = 4

new_salary = my_salary * (1 +(percent/100))
readjust_salary = new_salary - my_salary
print(f"Novo salario: {new_salary:.2f}\nReajuste ganho: {readjust_salary:.2f}\nEm percentual: {percent} %")
    