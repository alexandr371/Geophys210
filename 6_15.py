k=0
x=int(input())
while x!=0:
    k+=1
    p=x
    x=int(input())
    if x!=p and x!=0:
        k=0
print(k)