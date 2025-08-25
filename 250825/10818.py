# 최소, 최대

N = int(input())

l = list()
n = input().split()

for i in n:
    l.append(int(i))

print(min(l), max(l))
# print(min(n), max(n))