def prime_Decomposition(k):
    L = []
    L_num = []
    i = 2
    flag = 1
    while k >= i:
        if k % i == 0:
            if flag == 1:
                flag = 0
                k = k / i
                L.append(i)
                L_num.append(1)
            else:
                k = k / i
                L_num[-1] += 1
        else:
            flag = 1
            i += 1
    # print(L)
    # print(L_num)

    return L, L_num





