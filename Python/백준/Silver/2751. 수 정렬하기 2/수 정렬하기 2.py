import sys
mount = int(sys.stdin.readline())
lists = [0] * mount
for i in range(mount):
    lists[i] = int(sys.stdin.readline())
lists.sort()
print("\n".join(map(str,lists)))