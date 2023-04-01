# -*- coding: utf-8 -*-
# 入力
n = int(input())
list_w = list(input().split())
list_a = {"and", "not", "that", "the", "you"}
result = "No"
# 計算
for w in list_w:
    if w in list_a:
        result = "Yes"
        break
# 出力
print(result)