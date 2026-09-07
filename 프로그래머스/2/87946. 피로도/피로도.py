from itertools import permutations
def solution(k, dungeons):
    # 던전 개수 최대 8개라... 가지만 쳐도 괜찮다
    answer = -1
    # 전체 돌리는 법은 인덱스를 기록할까...? combination import가 있었던거 같은데
    for comb in permutations(dungeons, len(dungeons)):
        # print(comb)
        residue = k
        candidate = 0
        for a, b in comb:
            if a <= residue:
                residue -= b
                candidate += 1
            else:
                break
        if candidate > answer:
            answer = candidate
        # if answer == len(dungeons):
        #     break
                
                
    
    return answer