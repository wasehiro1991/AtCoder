# -*- coding: utf-8 -*-
# 入力
n, a, b = map(int, input().split())
result = 0

# 計算
for i in range(1, n + 1):
    tmp_i = i
    list_i = list(map(int, list(str(i))))
    tmp_add = sum(list_i)
    if a <= tmp_add <= b:
        result += i

# 出力
print(result)