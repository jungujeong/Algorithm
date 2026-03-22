import sys
input_list = list(map(int, sys.stdin.readline().split()))
input_list.sort()
a = input_list[1]
b = input_list[0]
def euclid(a:int, b:int):
    c = a%b
    if c == 0:
        return b
    a = max(b, c)
    b = min(b, c)
    return euclid(a, b)
mini = euclid(a, b)
print(mini)
print(int(a*b/mini))