import sys

row, column = map(int,sys.stdin.readline().rstrip().split())

matrixA = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(row)]
matrixB = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(row)]

for i in range(row):
    for j in range(column):
        print(matrixA[i][j] + matrixB[i][j], end=" ")
    print()