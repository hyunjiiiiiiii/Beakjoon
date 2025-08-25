# 영수증
N = list()
for j in range(10):
    N.append(int(input()))
print(N)

idx = 0
total = 0; sum = 0

for i in N:
    
    if idx == 0:
        total = i
        idx += 1
    else:
        sum += i
        idx += 1

print(total, sum)
print(total - sum)