value = int(input())

hundred_bills ,hundred_bills_rest  = int(value/100) ,value % 100
fifty_bills,  fifty_bills_rest = int(hundred_bills_rest/50), hundred_bills_rest % 50
twenty_bills, twenty_bills_rest = int(fifty_bills_rest/20), fifty_bills_rest % 20
ten_bills, ten_bills_rest = int(twenty_bills_rest/10), twenty_bills_rest % 10
five_bills, five_bills_rest = int(ten_bills_rest/5), ten_bills_rest % 5
two_bills, two_bills_rest = int(five_bills_rest/2), five_bills_rest % 2


print(f"{hundred_bills} nota(s) de R$ 100,00")
print(f"{fifty_bills} nota(s) de R$ 50,00")
print(f"{twenty_bills} nota(s) de R$ 20,00")
print(f"{ten_bills} nota(s) de R$ 10,00")
print(f"{five_bills} nota(s) de R$ 5,00")
print(f"{two_bills} nota(s) de R$ 2,00")
print(f"{two_bills_rest} nota(s) de R$ 1,00")
