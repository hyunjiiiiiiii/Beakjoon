# 24

H1, M1, S1 = map(int, input().split(":"))

H2, M2, S2 = map(int, input().split(":"))

if H1 > H2:
    H2 += 24

if S2 < S1 and M2 > 0:
    M2 -= 1
    S3 = S2 + 60 - S1
elif S2 < S1 and M2 == 0:
    H2 -= 1
    M2 = 59
    S3 = S2 + 60 - S1
else:
    S3 = S2 - S1

if M2 < M1:
    H1 -= 1
    M3 = M2 + 60 - M1
else:
    M3 = M2 - M1

print(f"{(H2-H1):02}:{M3:02}:{S3:02}")