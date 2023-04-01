# -*- coding: utf-8 -*-
# 入力
r,c = list(map(int, input().split()))
list_rc = []
list_rc2 = []
for _ in range(r):
    list_x = list(input())
    list_rc.append(list_x)
    list_rc2.append(list_x.copy())
# 計算
for i in range(len(list_rc)):
    list_r = list_rc[i]
    for j in range(len(list_r)):
        b = list_r[j]
        if b not in (".", "#"):
            list_rc2[i][j] = "."
            for k in range(1, int(b) + 1):
                i2m = i-k if i-k > 0 else 0
                i2p = i+k if i+k < len(list_rc) - 1 else len(list_rc) - 1
                j2m = j-k if j-k > 0 else 0
                j2p = j+k if j+k < len(list_r) - 1 else len(list_r) - 1
                list_rc2[i2m][j] = "."
                list_rc2[i2p][j] = "."
                list_rc2[i][j2m] = "."
                list_rc2[i][j2p] = "."
                if k < int(b):
                    list_rc2[i2m][j2m] = "."
                    list_rc2[i2p][j2m] = "."
                    list_rc2[i2m][j2p] = "."
                    list_rc2[i2p][j2p] = "."
# 出力
for i in range(len(list_rc2)):
    list_r = list_rc2[i]
    print("".join(list_r))