def generate_combinations(n, length):
    result = []

    def backtrack(arr, idx, remaining):
        if idx == length - 1:
            arr.append(remaining)
            result.append(arr[:])
            arr.pop()
            return

        for value in range(remaining + 1):
            arr.append(value)
            backtrack(arr, idx + 1, remaining - value)
            arr.pop()

    backtrack([], 0, n)
    return result

def solution(n, info):
    answer = info
    combinations = generate_combinations(n, 11)
    biggest_diff = 0
    for combination in combinations:
        score_diff = 0
        for i in range(11):
            if info[i] == combination[i] == 0:
                continue
            elif info[i] >= combination[i]:
                score_diff -= 10 - i
            elif info[i] < combination[i]:
                score_diff += 10 - i
        if score_diff > biggest_diff:
            answer = combination
            biggest_diff = score_diff
        elif score_diff == biggest_diff:
            for k in range(10,-1,-1):
                if answer[k] == 0 and combination[k] == 0:
                    continue
                elif answer[k] > combination[k]:
                    break
                elif answer[k] < combination[k]:
                    answer = combination
                    break
    if biggest_diff == 0:
        answer = [-1]
    
    return answer