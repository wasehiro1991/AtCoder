# -*- coding: utf-8 -*-
# 入力
n = input()
input_list = list(map(int, input().split()))
result = 0

def isCanDo(tmp_list:list):
    list_after = list(filter(lambda x: x%2==0, input_list))
    return len(list_after) == len(tmp_list)

# 計算
while isCanDo(input_list):
    input_list = list(map(lambda x: x//2, input_list))
    result+=1
# 出力
print(result)