a=[str(s) for s in input().split()]
b=[]
#print(a)
for i in range(len(a)):
    if a.count(a[i])==1:
        b.append(a[i])
#print(b)
print(' '.join(b))