import sys
count = int(sys.stdin.readline())
season = 666
count_n = 0
while(True):
    if '666' in str(season):
        count_n += 1
    if count_n == count:
        break
    season += 1
print(season)