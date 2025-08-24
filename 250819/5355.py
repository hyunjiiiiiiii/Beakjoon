# 화성 수학

T = int(input())

for i in range(1, T+1):
    put = input().split()

    num = float(put[0])
    put = put[1:]

    for j in put:
        if j == "@":
            num *= 3
        elif j == "%":
            num += 5
        elif j == "#":
            num -= 7

    # 소수점 둘째자리까지 표현
    print(f"{num:.2f}")



