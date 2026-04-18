def solution(n, words):
    answer = [0,0]
    # 무조건 brute force?
    # 끝말을 업데이트하면서 넘어가자. + 중복 단어 관리해야하니까 다 기록...
    # 인덱스+1 를 인원수로 나눈 몫으로 몇 번째 탈락인지 기록 (나누어 떨어지면 그대로, 그 이외는 + 1)
    # " 나머지로 몇 번째 선수인지 기록 (나머지가 0이면 맨 마지막에 해당)
    used_words = set()
    used_words.add(words[0])
    a, b = 0, 0
    m = len(words)
    k = len(words[0])
    last_letter = words[0][k-1]
    for i in range(1, m):
        word = words[i]
        if word[0] == last_letter and word not in used_words:
            used_words.add(word)
            last_letter = word[-1]
        else:
            if (i+1) % n == 0:
                a = n
                b = (i+1) // n
            else:
                a = (i+1) % n
                b = (i+1) // n + 1
            break
    answer[0] += a
    answer[1] += b
    return answer