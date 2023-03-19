# -*- coding: utf-8 -*-
# 入力
n = int(input())
list_a = list(input().split())
result = []
# 計算
for a in list_a:
    if int(a) % 2 == 0:
        result.append(a)
# 出力
print(' '.join(result))