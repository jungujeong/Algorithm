def solution(rsp):
    answer = ''
    ans_list = []
    winner = list(rsp)
    for i in winner:
        if i == '0':
            ans_list.append('5')
        elif i == '2':
            ans_list.append('0')
        else:
            ans_list.append('2')
        answer = "".join(ans_list)
    return answer