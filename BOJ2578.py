from collections import deque
board = [[int(i) for i in __import__('sys').stdin.readline().split()] for _ in range(5)]
check = [[False]*5 for _ in range(5)]
calls = deque()
for _ in range(5):
    for x in __import__('sys').stdin.readline().split():
        calls.append(int(x))
bingo = 0
f = False
for idx, call in enumerate(calls):
    if not f:
        for i in range(5):
            for j in range(5):
                if board[i][j] == call:
                    check[i][j] = True
                    if not (False in check[i]):
                        bingo += 1
                    if check[0][j] and check[1][j] and check[2][j] and check[3][j] and check[4][j]:
                        bingo += 1
                    if i == j:
                        if check[0][0] and check[1][1] and check[2][2] and check[3][3] and check[4][4]:
                            bingo += 1
                    if i == 4-j:
                        if check[0][4] and check[1][3] and check[2][2] and check[3][1] and check[4][0]:
                            bingo += 1

                    if bingo >= 3:
                        f = True
                        print(idx+1)
                        break
    else:
        break
