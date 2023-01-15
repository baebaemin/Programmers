def solution(numbers):
    num = 0
    for i in range(10):
        if i in tuple(numbers) != True:
            pass
        else:
            num = num + i
    print(num)

solution([1,2,3,4,6,7,8,0])