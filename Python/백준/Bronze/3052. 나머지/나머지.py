import sys
nam = [0]*42
for _ in range(10):
    nam[int(sys.stdin.readline())%42] += 1
count=0
for i in nam:
    if i != 0:
        count += 1
print(count)