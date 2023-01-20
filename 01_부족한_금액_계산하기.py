def solution(price, money, count):
    # price = 3, money = 20, count = 4
    fee = 0
    for i in range(1 + count):
        fee += price * i
    return 0 if money >= fee else fee - money

print(solution(3, 20 ,4))

# 다른 사람의 풀이
# def solution(price, money, count):
#    return max(0,price*(count+1)*count//2-money)