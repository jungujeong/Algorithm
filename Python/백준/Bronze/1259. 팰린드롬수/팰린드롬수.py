import sys
while True:
    num_str = sys.stdin.readline().rstrip()
    if num_str == '0':
        break
    if num_str == num_str[::-1]:
        print("yes")
    else:
        print("no")