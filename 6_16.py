k=0
x=int(input())
s=0
s_sq=0
while x!=0:
    k+=1
    s+=x
    s_sq=s_sq+x**2
    mean=s/k   
    x=int(input())
    if k!=1:
        std=((k*(mean**2)-mean*2*s+s_sq)/(k-1))**(1/2)
print(std)