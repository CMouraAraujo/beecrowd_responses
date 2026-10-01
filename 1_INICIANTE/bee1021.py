import math

value = float(input())
inter = int(value)
coins = int((value - inter) * 100)

hundred_bills ,hundred_bills_rest  = int(value/100) ,value % 100
fifty_bills,  fifty_bills_rest = int(hundred_bills_rest/50), hundred_bills_rest % 50
twenty_bills, twenty_bills_rest = int(fifty_bills_rest/20), fifty_bills_rest % 20
ten_bills, ten_bills_rest = int(twenty_bills_rest/10), twenty_bills_rest % 10
five_bills, five_bills_rest = int(ten_bills_rest/5), ten_bills_rest % 5
two_bills, two_bills_rest = int(five_bills_rest/2), int(five_bills_rest % 2)
fifty_coin, fifty_coin_rest = int(coins / 50), int(coins % 50)
twenty_five_coin, twenty_five_coin_rest = int(fifty_coin_rest / 25), int(fifty_coin_rest % 25)
ten_coin, ten_coin_coin_rest = int(twenty_five_coin_rest / 10), int(twenty_five_coin_rest % 10)
five_coin, five_coin_rest = int(ten_coin_coin_rest / 5), int(ten_coin_coin_rest % 5)

print("NOTAS:")
print(f"{hundred_bills} nota(s) de R$ 100.00")
print(f"{fifty_bills} nota(s) de R$ 50.00")
print(f"{twenty_bills} nota(s) de R$ 20.00")
print(f"{ten_bills} nota(s) de R$ 10.00")
print(f"{five_bills} nota(s) de R$ 5.00")
print(f"{two_bills} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{two_bills_rest} moeda(s) de R$ 1.00")
print(f"{fifty_coin} moeda(s) de R$ 0.50")
print(f"{twenty_five_coin} moeda(s) de R$ 0.25")
print(f"{ten_coin} moeda(s) de R$ 0.10")
print(f"{five_coin} moeda(s) de R$ 0.05")
print(f"{five_coin_rest} moeda(s) de R$ 0.01")
