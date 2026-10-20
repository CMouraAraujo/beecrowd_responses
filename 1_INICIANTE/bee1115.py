while True:
    coord_x, coord_y = map(int, input().split())
    
    if coord_x == 0 or coord_y == 0:
        break
    else:
        if coord_x > 0 and coord_y > 0:
            print("primeiro")
        elif coord_x > 0 and coord_y < 0:
            print("quarto")
        elif coord_x < 0 and coord_y > 0:
            print("segundo")
        else:
            print("terceiro")
            
