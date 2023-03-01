# -*- coding: utf-8 -*-
# 入力
N, M = map(int, input().split())
isMakableSeq = True
seq_base = []
xy_data_list = []
nomatch_data_list= []
for _ in range(M):
    tmp_tup = tuple(map(int, input().split()))

    if tmp_tup in xy_data_list:
        continue

    xy_data_list.append(tmp_tup)
    len_list = len(seq_base)
    if len_list == 0:
        seq_base.extend(tmp_tup)
        continue

    nomatch_data_list.append(tmp_tup)
    st, en = seq_base[0], seq_base[len_list - 1]
    for i in range(len(nomatch_data_list)):
        nomatch_data = nomatch_data_list[i]
        if st == nomatch_data[1]:
            seq_base.insert(0, nomatch_data[0])
            nomatch_data_list.pop(i)
        elif en == nomatch_data[0]:
            seq_base.append(nomatch_data[1])
            nomatch_data_list.pop(i)

if len(nomatch_data_list) > 0:
    isMakableSeq = False

sequence = []
if isMakableSeq:
    for i in range(1, N + 1):
        sequence.append(seq_base.index(i) + 1)

# 出力
print("Yes" if isMakableSeq else "No")
if isMakableSeq:
    print(*sequence, sep=" ")