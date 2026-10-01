AVG_CONSUMPTION = 12 #km/l

total_travel_time = int(input())
avg_speed = int(input())

total_distance = total_travel_time * avg_speed
travel_consumption = total_distance / AVG_CONSUMPTION

print(f"{travel_consumption:.3f}")
