import math

x1_p1, y1_p1 = map(float, input().split())
x2_p2, y2_p2 = map(float, input().split())

DISTANCE = math.sqrt(math.pow((x2_p2 - x1_p1), 2) + math.pow((y2_p2 - y1_p1), 2))

print(f"{DISTANCE:.4f}")