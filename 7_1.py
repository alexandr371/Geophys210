a=[int(s) for s in input().split()]
b=[]
for n in a:
    if n%2==0:
        b.append(str(n))
print(' '.join(b))