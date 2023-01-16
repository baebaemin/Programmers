def solution(n):
    for i in range(1, n // 2):
        if i * i == n:
            i += 1
            return i * i
            break
    if n == 1:
        return 4
    else:
        return -1