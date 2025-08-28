# 피보나치 수 2

n = int(input())

prev_1 = 0
prev_2 = 1

if n == 0:
    pb = prev_1

if n == 1:
    pb = prev_2

for i in range(2, n + 1):
    if i % 2 == 0:
        pb = prev_1 + prev_2
        prev_1 = pb
    else:
        pb = prev_1 + prev_2
        prev_2 = pb

print(pb)