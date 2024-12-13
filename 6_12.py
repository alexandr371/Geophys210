max=-10000000
max2=-10000000
x=int(input())
while x!=0:
    if x>max2:
        max2=x
    if x>max:
        max2=max
        max=x
    x=int(input())
print(max2)