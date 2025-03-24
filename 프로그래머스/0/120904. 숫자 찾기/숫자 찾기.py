def solution(num, k):
    list_num = list(str(num))
    
    return -1 if str(k) not in list_num else list_num.index(str(k))+1
    
    