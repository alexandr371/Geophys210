a=[int(s) for s in input().split()]
b=[]
for i in range(1, len(a)):
    if a[i]*a[i-1]>0:
        print(a[i-1], a[i])
        break