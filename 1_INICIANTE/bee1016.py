distance = int(input())

speed_first_car = 60
speed_second_car = 90

speed_difference = speed_second_car - speed_first_car
MINUTES_IN_ONE_HOUR = 60
value = MINUTES_IN_ONE_HOUR / speed_difference

print(f"{int(distance*value)} minutos")