n=int(input())
i=2
x=1
p=1
while x<n:
    x=x+p
    p=x-p
    i+=1
    #print(i, x, p)
if x==n:  
    print(i)
else:
    print(-1)