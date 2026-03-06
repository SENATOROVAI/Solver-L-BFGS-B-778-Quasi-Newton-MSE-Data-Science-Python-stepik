x, a, R = map(float, input().split())
d = abs(x - a)
inside_flag = 1 if d < R else 0
print('{:.6f} {}'.format(d, inside_flag))
