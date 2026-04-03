import sys
amount = int(sys.stdin.readline())
lists = []
for i in range(amount):
    lists.append(list(map(str, sys.stdin.readline().split())))
    lists[i][0] = int(lists[i][0])
    lists[i].insert(1, i)
lists.sort()
for i in range(amount):
    print(lists[i][0], lists[i][2])