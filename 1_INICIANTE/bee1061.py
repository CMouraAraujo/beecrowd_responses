import datetime

today = datetime.date.today()

start_day = str(input().replace('Dia ', ''))
start_hour, start_minute, start_second = list(input().split(" : "))

end_day = str(input().replace('Dia ', ''))
end_hour, end_minute, end_second = list(input().split(" : "))

start_date = datetime.datetime(day=int(start_day), hour=int(start_hour), minute=int(start_minute), second=int(start_second), year=today.year, month=today.month)
end_date = datetime.datetime(day=int(end_day), hour=int(end_hour), minute=int(end_minute), second=int(end_second), year=today.year, month=today.month)

interval = end_date - start_date 
days = int(interval.seconds/3600)
minutes = int((interval.seconds - (days * 3600))/60)
seconds = (interval.seconds%60)

print(f"{abs(interval.days)} dia(s)\n{days} hora(s)\n{minutes} minuto(s)\n{seconds} segundo(s)")