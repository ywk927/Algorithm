from itertools import combinations
def solution(relation):
    answer = 0
    r = len(relation) # 20개, r개의 값을 비교
    c = len(relation[0]) # 8개
    # 인덱스를 기록하기?
    answer_set = []
    for i in range(1,c+1):
        for comb in combinations(range(c), i): # 몇 번째 열(c)들을 보는지를 결정
            a = set()
            cnt = 0
            idx = True
            
            for candidate in answer_set:
                if set(candidate).issubset(set(comb)):
                    idx = False
                    break
            if idx:
                for k in range(r):
                    key = tuple(relation[k][column] for column in comb)
                    if key not in a:
                        a.add(key)
                        cnt += 1
                if cnt == r:
                    answer += 1
                    answer_set.append(comb)
            
    return answer