def power(a, n):
    res=1
    if n>=0:
        for i in range(n):
            res*=a
    if n<0:
        for i in range(abs(n)):
            res/=a
    return res
print(power(int(input()), int(input())))