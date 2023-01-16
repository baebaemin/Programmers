def solution(arr):
    num_list = list(map(int, arr))
    answer = sum(num_list) / len(num_list)
    return answer