# -*- coding: utf-8 -*-
# 入力
list_s = list(input())
result = []
# 計算
for i in range(len(list_s)):
    result.append(list_s[i].upper())
# 出力
print(''.join(result))