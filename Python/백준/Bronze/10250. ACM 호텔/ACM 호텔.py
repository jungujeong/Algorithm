import sys
T = int(sys.stdin.readline().rstrip())
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    floor = N%H if N%H!=0 else H
    num = (N-1)//H+1 if len(str((N-1)//H+1))==2 else '0'+ str((N-1)//H+1)
    print(f"{floor}{num}")