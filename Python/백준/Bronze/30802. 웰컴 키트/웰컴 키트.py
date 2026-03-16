import sys
people = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())
t_count = 0
for i in a:
    if i%t==0:
        t_count+=i//t
    else:
        t_count+=i//t+1
p_set = people//p
p_count = people % p
print(t_count)
print(f'{p_set} {p_count}')