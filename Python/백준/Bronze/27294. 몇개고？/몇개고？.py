import sys
rices = 280
t, s = map(int, sys.stdin.readline().split())
if 12 <= t and t <= 16 and s == 0:
    rices = 320
print(rices)