start_hour, end_hour = map(int, input().split())

if start_hour > end_hour:
    total = 24 - start_hour + end_hour
elif end_hour > start_hour:
    total = end_hour - start_hour
else:
    total = 24

print(f"O JOGO DUROU {total} HORA(S)")