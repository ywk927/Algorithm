def solution(s):
    answer = ''
    result = s.split(" ") # split을 " "로 하는게 핵심
    # 공백의 길이를 기록하는 방법에 대해 고민하기...
    # 공백의 개념은 무엇인고...
    
    lists= []
    for each in result:
        word = ""
        for j in range(len(each)):
            if j == 0:
                word += each[j].upper()
            else:
                word += each[j].lower()
        lists.append(word)
    answer = " ".join(lists)
    return answer