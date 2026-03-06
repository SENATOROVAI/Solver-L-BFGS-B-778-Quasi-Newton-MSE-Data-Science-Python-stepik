import math

a, x = map(float, input().split())
L = math.sin(a) + math.cos(a) * (x - a)
print('{:.6f}'.format(L))
