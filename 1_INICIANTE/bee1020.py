total_days = int(input())

total_years, rest_days = int(total_days / 365), total_days % 365
total_months, days = int(rest_days / 30), rest_days % 30

print(f"{total_years} ano(s)\n{total_months} mes(es)\n{days} dia(s)")