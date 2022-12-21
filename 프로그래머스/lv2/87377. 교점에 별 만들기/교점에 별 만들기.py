def solution(line):
    point = []
    max_x, max_y, min_x, min_y = -float('inf'), -float('inf'), float('inf'), float('inf')
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            A,B,E,C,D,F = *line[i], *line[j]
            Discriminator = A*D - B*C
            if Discriminator == 0:
                continue
    
            x = (B*F - E*D) / Discriminator
            y = (E*C - A*F) / Discriminator

            if not x.is_integer() or not y.is_integer():
                continue
                
            point.append((x, y))
            max_x, max_y, min_x, min_y = max(max_x, x), max(max_y, y), min(min_x, x), min(min_y, y)

    x_size, y_size = int(max_x - min_x + 1), int(max_y - min_y + 1)
    answer = [['.'] * x_size for _ in range(y_size)]
    for i in point:
        answer[int(i[1] - int(min_y))][int(i[0] - min_x)] = "*"
    return list(reversed(["".join(i) for i in answer]))