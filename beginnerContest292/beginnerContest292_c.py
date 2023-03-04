# -*- coding: utf-8 -*-
import math
# 入力
n = int(input())
result = 0
# 計算
for i in range(1, n):
    cnt_a = 0
    cnt_b = 0
    a = i
    b = n - i
    for j in range(1, int(math.sqrt(a)) + 1):
        if a % j == 0:
            cnt_a += 2 if a != j*j else 1
    for j in range(1, int(math.sqrt(b)) + 1):
        if b % j == 0:
            cnt_b += 2 if b != j*j else 1
    result += cnt_a * cnt_b
# 出力
print(result)