# -*- coding: utf-8 -*-
# 入力
n = int(input())
list_s = list(input())
list_now = [0, 0]
list_until = {(0, 0)}
isExitSame = False
# 計算
for moveTo in list_s:
    if moveTo == "R":
        list_now[0] = list_now[0] + 1
    if moveTo == "L":
        list_now[0] = list_now[0] - 1
    if moveTo == "U":
        list_now[1] = list_now[1] + 1
    if moveTo == "D":
        list_now[1] = list_now[1] - 1
    if tuple(list_now) in list_until:
        isExitSame = True
        break
    list_until.add(tuple(list_now.copy()))
# 出力
print("Yes" if isExitSame else "No")