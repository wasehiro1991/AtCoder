# -*- coding: utf-8 -*-
# 入力
n, x = list(map(int, input().split()))
tuple_a = tuple(map(int, input().split()))
dic_a = {s : s for s in tuple_a}
result = "No"

for a in tuple_a:
    n = a - x
    if n in dic_a:
        result = "Yes"
        break
# 出力
print(result)