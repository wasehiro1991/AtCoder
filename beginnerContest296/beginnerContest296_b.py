# -*- coding: utf-8 -*-
# 入力
list_a = ["a","b","c","d","e","f","g","h"]
list_rl = []
for i in range(1,9):
    list_r = []
    for j in range(8):
        list_r.append(list_a[j] + str(9 - i))
    list_rl.append(list_r)
for i in range(8):
    list_s = list(input())
    for j in range(8):
        if "*" == list_s[j]:
            result = list_rl[i][j]

# 出力
print(result)