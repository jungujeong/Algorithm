import sys
value = 1
while True:
    sum = 0
    value = int(sys.stdin.readline())
    if value == 0:
        break
    for i in range(1, value + 1):
        sum += i
    print(sum)