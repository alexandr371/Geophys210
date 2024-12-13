n=int(input())
i=2
x=2
p=1
while i!=n:
    
    x=x+p
    p=x-p
    i+=1
    print(i, p, x)
print(p)