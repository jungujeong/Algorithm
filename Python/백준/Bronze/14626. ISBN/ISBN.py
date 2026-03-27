import sys
num_input = list(sys.stdin.readline().rstrip())
m = int(num_input[12])
scratch_index = num_input.index('*')
eoro = 1
if scratch_index % 2 == 1:
    eoro = 3
num_input[scratch_index] = '0'
num = list(map(int, num_input))
even = sum(num[i] for i in range(0, 12, 2))
odd = sum(num[i] for i in range(1, 12, 2)) * 3
final_sum = even + odd
for i in range(0, 10):
    if (final_sum+eoro*i+m) % 10 == 0:
        print(i)
        break