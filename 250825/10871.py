# X보다 작은 수

N, X = map(int, input().split())

N_list = input().split()

small = list()
for i in N_list:
    if int(i) < X:
        small.append(int(i))
    else:
        continue

for j in small:
    print(j, end=' ')