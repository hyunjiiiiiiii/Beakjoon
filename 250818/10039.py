# 평균 점수

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

score = [A, B, C, D, E]
sum = 0

for i in score:
    if i >= 40:
        sum += i
    else:
        sum += 40

print(int(sum / 5))
