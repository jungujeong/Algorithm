import sys
tc = sys.stdin.readline().rstrip()
count = [-1]*26
for i in range(len(tc)):
    if count[ord(tc[i])-97] == -1:
        count[ord(tc[i])-97] += 1+i
print(" ".join(list(map(str,count))))
