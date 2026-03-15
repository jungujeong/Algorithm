import sys
tc = int(sys.stdin.readline())
for _ in range(tc):
    ans = sys.stdin.readline().rstrip()
    score = 0
    streak = 0
    for i in ans:
        if i == 'O':
            streak += 1
            score += streak
        else:
            streak = 0
    print(score)