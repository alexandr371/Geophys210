a=[int(s) for s in input().split()]
b=[]
for i in range(1, len(a)):
    if a[i]>a[i-1]:
        b.append(str(a[i]))
print(' '.join(b))