def solution(k, tangerine):
    answer = 0
    dic = {}
    for each in tangerine:
        if each in dic:
            dic[each] += 1
        else:
            dic[each] = 1
    result = sorted(dic.items(), key = lambda x: x[1], reverse = True)
    # print(result)
    for x, y in result:
        answer += 1
        k -= y
        if k <= 0:
            break
    return answer