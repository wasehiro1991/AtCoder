# -*- coding: utf-8 -*-
# 入力
n = int(input())
list_s = list(input())
result = True

# 計算
for i in range(1, n):
    s1 = list_s[i-1]
    s2 = list_s[i]
    if s1 == s2:
        result = False
# 出力
print("Yes" if result else "No")