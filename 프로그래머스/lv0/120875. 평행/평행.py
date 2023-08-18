def solution(dots):
    dot_idx = [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2]]
    for idx in dot_idx:
        a, b, c, d = dots[idx[0]], dots[idx[1]], dots[idx[2]], dots[idx[3]]
        x_grad_1 = abs(a[0] - b[0])
        y_grad_1 = abs(a[1] - b[1])
        x_grad_2 = abs(c[0] - d[0])
        y_grad_2 = abs(c[1] - d[1])
        if x_grad_1 / y_grad_1 == x_grad_2 / y_grad_2:
            return 1
    return 0