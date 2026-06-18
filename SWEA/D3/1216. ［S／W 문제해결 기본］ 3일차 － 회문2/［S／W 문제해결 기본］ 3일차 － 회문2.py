def isWidthPalindrome(i,j, length):
    #가로 (열)
    idx = True
    if length % 2 == 1:
        mid = j + length // 2
        for k in range(1,((length-1) // 2) + 1):
            if arr[i][mid-k] != arr[i][mid+k]:
                idx = False
                break
    elif length % 2 == 0:
        mid = j + length // 2
        if arr[i][mid] == arr[i][mid-1]:
            for k in range(1, ((length - 2) // 2) + 1):
                if arr[i][mid - k - 1] != arr[i][mid + k]:
                    idx = False
                    break
        else:
            idx = False
    if idx:
        return length

def isHeightPalindrome(i, j, length):
    #세로 (행)
    idx = True
    if length % 2 == 1:
        mid = i + length // 2
        for k in range(1,((length-1) // 2) + 1):
            if arr[mid-k][j] != arr[mid+k][j]:
                idx = False
                break
    elif length % 2 == 0:
        mid = i + length // 2
        if arr[mid-1][j] == arr[mid][j]:
            for k in range(1, ((length - 2) // 2) + 1):
                if arr[mid-k-1][j] != arr[mid+k][j]:
                    idx = False
                    break
        else:
            idx = False
    if idx:
        return length

for tc in range(1,11):
    idx = True
    N = int(input())
    arr = [list(input()) for _ in range(100)]
    found = False
    # print(arr)
    # 길이가 가장 긴 100개 부터 거꾸로 찾아 나가기
    longest_len = 100
    while longest_len >= 1:
        if found:
            break
        for i in range(100):
            if found:
                break
            for j in range(100-longest_len+1):
                if isWidthPalindrome(i, j, longest_len):
                    print(f'#{N} {longest_len}')
                    found = True
                    break
        if found:
            break
        for i in range(100-longest_len+1):
            if found:
                break
            for j in range(100):
                if isHeightPalindrome(i, j, longest_len):
                    print(f'#{N} {longest_len}')
                    found = True
                    break
        longest_len -= 1