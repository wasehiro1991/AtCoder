# -*- coding: utf-8 -*-
# 入力
n, m = list(map(int, input().split()))
result = -1
is_exist = False
j1 = 1
j2 = n

for i in range(1, n + 1):
    if i * n == m:
        result = i * n
        is_exist = True
        break
    if n * n < m:
        break
    if i * n > m:
        j1 = i
        j2 = (i + n) // 2 
        break

while not is_exist:
    if i * j2 < m:
        j1 = j2
        j2 = (j1 + n) // 2
# 出力
print(result)