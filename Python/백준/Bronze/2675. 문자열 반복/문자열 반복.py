import sys
t = int(sys.stdin.readline())
for _ in range(t):
    r, s = sys.stdin.readline().split()
    for i in s:
        print(i*int(r),end="")
    print()