import sys
count = int(sys.stdin.readline())
for _ in range(count):
    answer = True
    sentence = list(sys.stdin.readline().rstrip())
    stack = []
    for w in sentence:
        if w == "(":
            stack.append(w)
        if w == ")":
            if len(stack) == 0 or stack.pop() != "(":
                answer = False
                break
    if answer and len(stack) == 0:
        print("YES")
    else:
        print("NO")