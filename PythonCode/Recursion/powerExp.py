# power of a base to e using recursion


def power(b,e):
    if(e == 0 ): return 1
    return b * power(b,e-1)



val = power(2,4)
print(val)