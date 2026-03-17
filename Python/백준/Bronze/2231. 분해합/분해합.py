import sys

n = sys.stdin.readline().rstrip()
len = len(n)
ans = 0
if int(n)<19:
    for i in range(1, int(n)+1):
        if i + sum(int(j) for j in str(i)) == int(n):
            ans = i
            break
else:
    for i in range(int(n)-9 * len, int(n)+1):
        if i + sum(int(j) for j in str(i)) == int(n):
            ans = i
            break
print(ans)