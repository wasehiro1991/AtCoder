# -*- coding: utf-8 -*-
# 入力
s = input()
result = 0
# 計算
for i in range(1, len(s)):
    i2 = i * 2
    if i2 > len(s):
        break

    for j in range(len(s) - i2 + 1):
        w = s[j : j + i2]
        dic_count = {}
        for w2 in tuple(w):
            if w2 in dic_count:
                dic_count[w2] += 1
            else:
                dic_count.update({w2 : 1})
        isHappy = True
        for val in dic_count.values():
            if val % 2 == 1:
                isHappy = False
                break
        if isHappy:
            result += 1
# 出力
print(result)