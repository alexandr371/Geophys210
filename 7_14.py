n, k=[int(s) for s in input().split()]
a=['I']*n
#a=[int(i) for i in range(1, n+1)]
for i in range(k):
    l, r=[int(s) for s in input().split()]
    a[l-1:r]='.'*(r-l+1)
    #print(a)
print(''.join(a))