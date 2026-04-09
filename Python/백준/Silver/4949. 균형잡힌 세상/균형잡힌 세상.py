import sys
while(True):
    answer = True
    sentence = list(sys.stdin.readline().rstrip())
    if sentence[0] == ".":
        break
    stack = []
    for w in sentence:
        if w == "(" or w == "[":
            stack.append(w)
        if w == ")":
            if len(stack) == 0 or stack.pop() != "(":
                answer = False
                break
        if w == "]":
            if  len(stack) == 0 or stack.pop() != "[":
                answer = False
                break
    if answer and len(stack) == 0:
        print("yes")
    else:
        print("no")