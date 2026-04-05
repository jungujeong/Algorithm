import sys
amount = int(sys.stdin.readline())
lists = []
for _ in range(amount):
    a, b = map(int, sys.stdin.readline().split())
    lists.append([b, a])
lists.sort()
for i in range(amount):
    print(lists[i][1], lists[i][0])