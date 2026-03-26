import sys
a, b = map(int,sys.stdin.readline().split())
def fact(num:int):
    sum_ = 1
    for i in range(1, num+1):
        sum_ *= i
    return sum_
print(fact(a)//(fact(b)*fact(a-b)))