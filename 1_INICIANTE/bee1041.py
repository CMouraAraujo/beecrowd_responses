coord_X, coord_Y = map(float, input().split())

if coord_X > 0 and coord_Y > 0:
    print("Q1")
elif coord_X > 0 and coord_Y < 0:
    print("Q4")
elif coord_X < 0 and coord_Y > 0:
    print("Q2")
elif coord_X < 0 and coord_Y < 0:
    print("Q3")
elif coord_X == 0 and coord_Y != 0:
    print("Eixo Y")
elif coord_Y == 0 and coord_X != 0:
    print("Eixo X")
else:
    print("Origem")