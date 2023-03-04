# -*- coding: utf-8 -*-
# 入力
n, q = list(map(int, input().split()))
player = [[0, 0] for _ in range(n)]
# 計算
for _ in range(q):
    event = list(map(int, input().split()))
    if event[0] == 1:
        player[event[1] - 1][0] += 1
    if event[0] == 2:
        player[event[1] - 1][1] += 1
    if event[0] == 3:
        isDead = False
        if player[event[1] - 1][0] == 2 or player[event[1] - 1][1] == 1:
            isDead = True
        print("Yes" if isDead else "No")
# 出力