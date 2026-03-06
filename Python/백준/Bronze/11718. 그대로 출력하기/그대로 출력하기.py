import sys
for i in range(100):
    try:
        print(sys.stdin.readline(),end="")
    except EOFError:
        break