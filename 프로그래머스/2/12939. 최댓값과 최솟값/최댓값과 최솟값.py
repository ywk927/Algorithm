def solution(s):
    answer = ''
    numbers = s.split()
    # str type이어도 대소 자체는 비교 가능 -> 당연한거... 근데 문자열로 비교하면 음수는 반대의 결과가 나옴. 그냥 type 변환시켜? 최적화는 아님
    min_num = int(numbers[0])
    max_num = int(numbers[0])
    for num in numbers:
        if int(num) < int(min_num):
            min_num = int(num)
        if int(num) > int(max_num):
            max_num = int(num)
    answer += str(min_num)
    answer += " "
    answer += str(max_num)
    return answer