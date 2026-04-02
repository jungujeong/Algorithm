import sys
mount = int(sys.stdin.readline())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(mount)]
for i in range(mount):
    rank = 1
    for j in range(mount):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    print(rank ,end = " ")