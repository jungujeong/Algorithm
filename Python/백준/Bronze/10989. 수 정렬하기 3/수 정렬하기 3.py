import sys
count = int(sys.stdin.readline())
num_list = [0]*10001
for _ in range(count):
    num_list[int(sys.stdin.readline())] += 1
for i in range(len(num_list)):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i)