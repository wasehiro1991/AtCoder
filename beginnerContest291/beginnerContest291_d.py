# -*- coding: utf-8 -*-
# 入力
N = int(input())
data_card = [tuple(map(int, input().split())) for _ in range(N)]
data_fb = [[0, 0] for _ in range(N)]
data_fb[0] = [1, 1]
MOD = 998244353

# 計算
for i in range(1, N):
    if data_card[i][0] != data_card[i-1][0]:
        data_fb[i][0] += data_fb[i-1][0]
    if data_card[i][0] != data_card[i-1][1]:
        data_fb[i][0] += data_fb[i-1][1]
    if data_card[i][1] != data_card[i-1][0]:
        data_fb[i][1] += data_fb[i-1][0]
    if data_card[i][1] != data_card[i-1][1]:
        data_fb[i][1] += data_fb[i-1][1]
    data_fb[i][0]%=MOD
    data_fb[i][1]%=MOD

# 出力
print((data_fb[N-1][0] + data_fb[N-1][1]) % MOD)