import sys
sound = list(map(int, sys.stdin.readline().split()))
for i in range(7):
    if sound[i]+1==sound[i+1]:
        pass
    else:
        for i in range(7):
            if sound[i]-1==sound[i+1]:
                pass
            else:
                print("mixed")
                sys.exit()
        print("descending")
        sys.exit()
print("ascending")