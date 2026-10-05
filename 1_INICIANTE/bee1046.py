start_hour, start_minute, end_hour, end_minute = map(int, input().split())
total_hours = 24

if start_hour > end_hour:
    total_hours = 24 - start_hour + end_hour
    if start_minute < end_minute:
        total_minutes = end_minute - start_minute
    elif start_minute > end_minute:
        total_minutes = 60 - start_minute + end_minute
        total_hours -= 1
    elif start_minute == end_minute:
            total_minutes = end_minute
        
elif end_hour > start_hour:
    total_hours = end_hour - start_hour
    if start_minute < end_minute:
        total_minutes = end_minute - start_minute
    elif start_minute > end_minute:
        total_minutes = 60 - start_minute + end_minute
        total_hours -= 1
    elif start_minute == end_minute:
        total_minutes = end_minute

if start_hour == end_hour:
    if start_minute == end_minute:
        total_hours = 24
        total_minutes = 0
    elif start_minute < end_minute:
            total_hours = 0
            total_minutes = end_minute - start_minute
    elif start_minute > end_minute:
        total_minutes = 60 - start_minute + end_minute
        total_hours -= 1

    
print(f"O JOGO DUROU {total_hours} HORA(S) E {total_minutes} MINUTO(S)")