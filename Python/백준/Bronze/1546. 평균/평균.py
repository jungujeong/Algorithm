import sys
count = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a_sum = 0
print(sum(i for i in a)/max(a)*100/count)