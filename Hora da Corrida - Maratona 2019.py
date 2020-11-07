import math

v, n = list(map(int, input().split(' ')))

print(math.ceil(v*n*0.1), end=' ')
print(math.ceil(v*n*0.2), end=' ')
print(math.ceil(v*n*0.3), end=' ')
print(math.ceil(v*n*0.4), end=' ')
print(math.ceil(v*n*0.5), end=' ')
print(math.ceil(v*n*0.6), end=' ')
print(math.ceil(v*n*0.7), end=' ')
print(math.ceil(v*n*0.8), end=' ')
print(math.ceil(v*n*0.9))