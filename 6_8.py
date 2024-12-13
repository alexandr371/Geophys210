max=-10000000
x=int(input())
while x!=0:
    max=x if x>=max else max
    x=int(input())
print(max)