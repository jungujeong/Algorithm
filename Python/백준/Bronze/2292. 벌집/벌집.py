import sys
count = 1
jump = 6
n = int(sys.stdin.readline())
i=2
while(i <= n):
    count += 1
    if n < i + jump:
        break
    i += jump
    jump += 6
print(count)