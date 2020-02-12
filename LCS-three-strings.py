def lcs3(a, b, c):
    m = len(a)
    l = len(b)
    n = len(c)
    subs = [[[0 for k in range(n+1)] for j in range(l+1)] for i in range(m+1)]

    for i, x in enumerate(a):
        for j, y in enumerate(b):
            for k, z in enumerate(c):
                if x == y and y == z:
                    subs[i+1][j+1][k+1] = subs[i][j][k] + 1
                else:
                    subs[i+1][j+1][k+1] = max(subs[i+1][j+1][k],
                                              subs[i][j+1][k+1],
                                              subs[i+1][j][k+1])
    # return subs[-1][-1][-1] #if you only need the length of the lcs
    lcs = ""
    while m > 0 and l > 0 and n > 0:
        step = subs[m][l][n]
        if step == subs[m-1][l][n]:
            m -= 1
        elif step == subs[m][l-1][n]:
            l -= 1
        elif step == subs[m][l][n-1]:
            n -= 1
        else:
            lcs += str(a[m-1])
            m -= 1
            l -= 1
            n -= 1

    return lcs[::-1]