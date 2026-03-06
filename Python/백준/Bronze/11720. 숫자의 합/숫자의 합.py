import sys
count = int(sys.stdin.readline())
num = sys.stdin.readline()
s=0
for i in range(count):
    s+=int(num[i])
print(s)