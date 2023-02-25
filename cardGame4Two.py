# -*- coding: utf-8 -*-
# 入力
n = int(input())
list_a:list = list(map(int, input().split()))
total_alice = 0
total_bob = 0
result = 0

# 計算
for i in range(len(list_a)):
    max_a = max(list_a)
    if i % 2 == 0:
        total_alice += max_a
    else:
        total_bob += max_a
    list_a.remove(max_a)

result = total_alice - total_bob

# 出力
print(result)