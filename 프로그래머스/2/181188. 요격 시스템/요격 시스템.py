def solution(targets):
    answer = 0
    n = len(targets)
#     10, 14
#     11, 13
#     5, 12
    
#     4, 8
#     3, 7
#     4, 5
    
#     1,4
    for target in targets:
        target[0], target[1] = target[1], target[0]
    targets.sort()
    for target in targets:
        target[0], target[1] = target[1], target[0]
    last = -1
    for start, end in targets:
        if last <= start:
            answer += 1
            last = end
    # i = n-1
    # start_idx, end_idx = targets[i][0], targets[i][1]
    # original_start = start_idx
    # i -= 1
    # while i >= 0:
    #     new_start, new_end = targets[i][0], targets[i][1]
    #     if start_idx < new_end and new_end > original_start:
    #         start_idx = new_start
    #         if i == 0:
    #             answer += 1
    #         i -= 1
    #     else:
    #         answer += 1
    #         start_idx, end_idx = targets[i][0], targets[i][1]
    #         original_start = start_idx
    #         # print('hi')
    #         # print(start_idx, end_idx)
    #         if i == 0:
    #             answer += 1
    #         i -= 1
        
    return answer