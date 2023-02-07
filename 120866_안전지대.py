board_lst = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 1, 1, 0],
             [0, 0, 0, 0, 0]]


def solution(board):
    # 8방향 검사를 위한 리스트 생성
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    N = len(board)
    points = []  # 지뢰의 포인트를 담을 리스트 생성

    for r in range(N):
        for c in range(N):
            if board[r][c]:  # 지뢰가 묻혀있다면
                points.append([r, c])  # 리스트에 추가
                if len(points) > N * N - 8:  # 런타임 초과를 막기위한 조건
                    return 0

    for p in points:  # 지뢰 개수만큼 반복
        for i in range(8):  # 8방으로 델타 검사
            idr, idc = p[0] + dr[i], p[1] + dc[i]
            if 0 <= idr < N and 0 <= idc < N:  # 인덱스를 벗어나지 않는 조건으로
                board[idr][idc] = 1  # board에 X표기

    cnt = 0
    for r in range(N):
        for c in range(N):
            if not board[r][c]:  # 안전지대라면
                cnt += 1  # cnt 누적
    return cnt

print(solution(board_lst))