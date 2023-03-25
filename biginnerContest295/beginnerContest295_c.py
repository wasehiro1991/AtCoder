# -*- coding: utf-8 -*-
# 入力
n = int(input())
list_a = list(input().split())
dic_count = {}
result = 0
# 計算
for a in list_a:
    if a in dic_count:
        dic_count[a] += 1
    else:
        dic_count.update({a : 1})
for value in dic_count.values():
    result += value // 2
# 出力
print(result)