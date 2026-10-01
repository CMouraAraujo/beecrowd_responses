total_seconds = int(input())

seconds = total_seconds % 60 # Segundos restantes

total_minutes = int(total_seconds/60)
minutes = total_minutes % 60
hours = int(total_minutes / 60)

print(f"{hours}:{minutes}:{seconds}")