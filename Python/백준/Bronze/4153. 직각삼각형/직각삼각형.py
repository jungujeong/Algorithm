import sys
while(True):
    a, b, c = map(int, sys.stdin.readline().split())
    if a==b==c==0:
        break
    arr = sorted([a, b, c])
    if arr[0]**2+arr[1]**2 == arr[2]**2:
        print("right")
    else:
        print("wrong")