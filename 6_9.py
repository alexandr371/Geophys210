max=-10000000
k=0
x=int(input())
while x!=0:
    if x>max:
        max=x
        i=k
    x=int(input())
    k+=1
print(i)