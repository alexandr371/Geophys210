a=[int(s) for s in input().split()]
b=[]
for i in range(0,len(a), 2):
    b.append(str(a[i]))
print(b)
print(' '.join(b))