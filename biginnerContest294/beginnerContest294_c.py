# -*- coding: utf-8 -*-
# 入力
n, m = list(map(int, input().split()))
list_ab = []
for _ in range(2):
    list_ab.append(list(map(int, input().split())))
# list_c:list = sorted(list_ab[0] + list_ab[1])
list_c:list = list_ab[0].copy()
list_c.extend(list_ab[1])
list_c.sort()
get_index = {c: i + 1 for i, c in enumerate(list_c)}
# 計算
for ab in list_ab:
    list_idx = []
    for i in range(len(ab) - 1):
        print(get_index[ab[i]], end=" ")
    print(get_index[ab[len(ab) - 1]], end="\n")
# 出力