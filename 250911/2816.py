# 디지털 티비

N = int(input())

ch_list = []

for i in range(N):
    ch_list.append(input())



#print(ch_list)
idx = 0
for j in ch_list:
    
    if j == "KBS1":
        idx_1 = idx
        ch_list.remove("KBS1")
        ch_list.insert(0, "KBS1")
        break
    else:
        idx += 1
        continue

#print(ch_list)

idx = 0
for j in ch_list:
    if j == "KBS2":
        idx_2 = idx
        break
    else:
        idx += 1
        continue


print("1" * idx_1 + "4" * idx_1, end="")
print("1" * idx_2 + "4" * (idx_2-1))
