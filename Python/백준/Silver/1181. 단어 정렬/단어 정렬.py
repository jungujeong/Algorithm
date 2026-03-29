import sys
times = int(sys.stdin.readline())
lists = [sys.stdin.readline().rstrip() for _ in range(times)]
lists = list(set(lists))
lists.sort()
lists.sort(key=len)
print("\n".join(lists))