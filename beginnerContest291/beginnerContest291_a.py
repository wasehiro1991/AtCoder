# -*- coding: utf-8 -*-
# 入力
list_s = list(input())
result = 0
# 計算
for char in list_s:
    if char.isupper():
        result = list_s.index(char) + 1
        break
# 出力
print(result)