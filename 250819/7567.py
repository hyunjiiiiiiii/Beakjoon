# 그릇

dish = list(input())

h = 0
inx = 0

prev = dish[0]

while inx < len(dish):
    if inx == 0:
        h += 10
        inx += 1

    else:
        if prev == dish[inx]:
            h += 5
            prev = dish[inx]

        else:
            h += 10
            prev = dish[inx]

        inx += 1
print(h)