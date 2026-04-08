import sys
n = int(sys.stdin.readline())
bag = 0
while n>2:
    if n%5 == 0:
        bag += n//5
        n = 0
        break
    else:
        n -= 3
        bag += 1
if n == 0:
    print(bag)
else:
    print(-1)