import sys
count = int(sys.stdin.readline())
lists = []
for _ in range(count):
    value = int(sys.stdin.readline())
    if value == 0:
        lists.pop()
    else:
        lists.append(value)
sum_ = 0
for i in lists:
    sum_ += i
print(sum_)