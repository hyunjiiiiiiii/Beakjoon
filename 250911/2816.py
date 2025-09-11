# 디지털 티비

N = int(input())

ch_list = []

for i in range(N):
    ch_list.append(input())

idx = 0

for j in ch_list:
    if j == "KBS1":
        idx_1 = idx
    elif j == "KBS2":
        idx_2 = idx
    else:
        continue

print()