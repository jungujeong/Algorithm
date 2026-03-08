import sys
a=[]
for i in range(9):
    a.append(int(sys.stdin.readline().rstrip()))
high = max(a)
index = a.index(high)
print(high)
print(index+1)