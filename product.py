# -*- coding: utf-8 -*-
# 入力
a, b = map(int, input().split())
# 計算
mult_result = a * b
# 出力
if (0 == mult_result % 2) :
    print("Even")
else :
    print("Odd")
