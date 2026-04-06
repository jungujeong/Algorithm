import sys
amount_N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
amount_A = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
s = set(n)
for i in a:
    if i in s:
        print(1)
    else:
        print(0)