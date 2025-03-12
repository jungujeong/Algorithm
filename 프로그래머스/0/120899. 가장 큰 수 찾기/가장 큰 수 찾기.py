def solution(array):
    biggest = max(array)
    answer = [biggest, array.index(biggest)]
    return answer