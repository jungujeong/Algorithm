def solution(my_string):
    answer = 0
    my_list = list(my_string)
    my_list.sort()
    try:
        for i in my_list:
            answer+=int(i)
        return answer    
    except:
        pass
    return answer