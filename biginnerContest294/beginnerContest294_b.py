# -*- coding: utf-8 -*-
# 入力
h, w = list(map(int, input().split()))
list_a_i = []
for i in range(h):
    list_a_j = list(map(int, input().split()))
    list_a_i.append(list_a_j)
# 計算
for a_i in list_a_i:
    result = []
    for a_j in a_i:
        if a_j == 0:
            result.append(".")
        else :
            o = ord("A") + a_j - 1
            char = chr(o)
            result.append(char)
    print(''.join(result))
# 出力