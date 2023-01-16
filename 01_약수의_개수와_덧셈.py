def solution(left, right):
    sum = 0
    for i in range(left, right + 1):
        divisor = []
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                divisor.append(j)
        if len(divisor) % 2 == 0:
            sum = sum + i
        else:
            sum = sum -i
                
    return -sum

# -sum이 왜 정답인지 모르겠다 -.-