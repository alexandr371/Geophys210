k=0
p=10000000
x=int(input())
while x!=0:
    if x>p:
        k+=1
    p=x
    x=int(input())
print(k)