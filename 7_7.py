a=[int(s) for s in input().split()]
p=int(input())
i=0
while p<=a[i]:
    i+=1
    if i==len(a):
        break
print(i+1)