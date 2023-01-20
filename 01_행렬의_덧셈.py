def solution(arr1, arr2):
    lst = arr1
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            lst[i][j] = arr1[i][j] + arr2[i][j]
    return lst

print(solution([[1], [2]], [[3], [4]]))