import sys
amount = int(sys.stdin.readline())
lists = []
for _ in range(amount):
    lists.append(list(map(int, sys.stdin.readline().split())))
lists.sort()
for i in range(amount):
    print(lists[i][0], lists[i][1])