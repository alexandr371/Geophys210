a=[int(s) for s in input().split()]
a.append(0)
b=[int(s) for s in input().split()]
k=b[0] 
c=b[1]
for i in range(len(a)-1, k, -1):
    #print(i)
    a[i], a[i-1]=a[i-1], a[i]
a[k]=c
a.pop()
print(' '.join([str(s) for s in a]))