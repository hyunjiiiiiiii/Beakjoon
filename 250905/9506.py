# 약수들의 합

while True:
    n = int(input())

    if n == -1:
        break

    n_list=list()
    sum = 1

    for i in range(2, n):
        if n % i == 0:
            n_list.append(i)
    #print(n_list)

    for j in n_list:
        sum += j
    #print(sum)

    if sum == n:
        print(f"{n} = 1", end="")
        for value in n_list:
            print(f" + {value}", end="")
        print("")

    else:
        print(f"{n} is NOT perfect.")
