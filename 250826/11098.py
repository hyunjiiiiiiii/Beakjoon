# 첼시를 도와줘!

n = int(input())

for i in range(n):
    p = int(input())
    dict = {}
    for j in range(p):
        key, value = input().split()
        dict[int(key)] = value
    #print(dict)

    max_value = max(dict.keys())
    #rint(max_value)
    print(dict[max_value])