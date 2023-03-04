# -*- coding: utf-8 -*-
# 入力
n = int(input())
result = 0
# 計算
for i in range(1, n):
    cnt_a = 0
    cnt_b = 0
    b = n - i
    for j in range(1, i + 1):
        if j * j > i:
            break
        if i % j == 0:
            cnt_a += 2 if i != j*j else 1
    for j in range(1, b + 1):
        if j * j > b:
            break
        if b % j == 0:
            cnt_b += 2 if b != j*j else 1
    result += cnt_a * cnt_b
# 出力
print(result)