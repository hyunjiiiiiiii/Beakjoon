# 더하기 사이클

N = int(input())
prev = N
i = 0

while True:

    one = prev % 10   # 나머지
    ten = (prev - one) // 10   # 몫
    # print(prev, ten, one)
    sum = (one + ten) % 10
    new = one * 10 + sum
    # print(sum, new)
    #print(prev, new)

    if N == new:
        print(i+1)
        break
    else:
        i += 1
        prev = new
