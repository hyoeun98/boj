def solution(park, routes):
    answer = []
    W, H = len(park[0]), len(park)
    for i, row in enumerate(park):
        for j, col in enumerate(row):
            if col == "S":
                current_y, current_x = i, j
    
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        if direction == "E":
            if current_x + distance >= W:
                continue
            elif "X" in park[current_y][current_x:current_x + distance + 1]:
                continue
            else:
                current_x += distance
    
        elif direction == "W":
            if current_x - distance < 0:
                continue
            elif "X" in park[current_y][current_x - distance:current_x]:
                continue
            else:
                current_x -= distance
                
        elif direction == "S":
            if current_y + distance >= H:
                continue
            elif "X" in list(map(lambda x: x[current_x], park[current_y:current_y + distance + 1])):
                continue
            else:
                current_y += distance
            
        else:
            if current_y - distance < 0:
                continue
            elif "X" in list(map(lambda x: x[current_x], park[current_y - distance:current_y])):
                continue
            else:
                current_y -= distance

    return [current_y, current_x]