def no_same_num(arr):
    answer = []
    cnt = 1

    for i in arr:
        if i != arr[cnt]:
            answer.append(i)
        cnt += 1
        if cnt == len(arr):
            break

    if arr[-1] == arr[-2]:
        answer.append(arr[-1])
    return answer

array = [4, 4, 4, 3, 3]
print(no_same_num(array))