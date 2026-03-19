import sys
R = 31
M = 1234567891
l = int(sys.stdin.readline())
sentence = sys.stdin.readline().rstrip()
summ = 0
for i in range(l):
    summ += (ord(sentence[i])-ord('a')+1) * R**(i)
ans = summ%M
print(ans)