import sys
li = ['']*3
for i in range(3):
    li[i] = sys.stdin.readline().rstrip()
    if li[i].isdigit():
        num_index = i 
ans_num = int(li[num_index]) + 3 - num_index
ans = ''
if ans_num%3 == 0:
    ans += 'Fizz'
if ans_num%5 == 0:
    ans += 'Buzz'
if ans == '':
    ans = ans_num
print(ans)