import sys
size = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
print(f"{min(a)} {max(a)}")