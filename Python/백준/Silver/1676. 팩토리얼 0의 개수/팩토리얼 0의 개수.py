import sys
import math
num = int(sys.stdin.readline())
fac = math.factorial(num)
count = 0
temp = 0
while fac%10 == 0:
    fac = fac//10
    count += 1
print(count)
