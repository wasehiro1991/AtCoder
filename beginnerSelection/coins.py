# -*- coding: utf-8 -*-
# 入力
a = int(input())
b = int(input())
c = int(input())
x = int(input())
result = 0

# 計算
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            if i * 500 + j * 100 + k * 50 == x:
                result += 1

# 出力
print(result)