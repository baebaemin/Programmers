# def solution(arr1, arr2):
#     lst = arr1
#     for i in range(len(arr1)):
#         for j in range(len(arr1[i])):
#             lst[i][j] = arr1[i][j] + arr2[i][j]
#     return lst

# print(solution([[1,2], [2,3]], [[3,4], [5,6]]))

# zip()을 이용해 풀어보기
def solution(arr1, arr2):
    return [[sum(pair) for pair in zip(a, b)] for a, b in zip(arr1, arr2)]

solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])