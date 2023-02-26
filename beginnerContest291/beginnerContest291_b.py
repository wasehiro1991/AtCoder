# -*- coding: utf-8 -*-
# 入力
n = int(input())
list_x = list(map(int, input().split()))
result = 0
# 計算
for i in range(n):
    max_x = max(list_x)
    list_x.remove(max_x)
    min_x = min(list_x)
    list_x.remove(min_x)
result = sum(list_x) / (3 * n)
# 出力
print(result)