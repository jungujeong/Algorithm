import sys
count = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in n_list:
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(i**0.5)+1):
        if i%j==0:
            is_prime = False
            break
    if is_prime==True:
        ans+=1
print(ans)