n=int(input())
a=1
for i in range(1, n):
    a=a*int(input())
f=1
for i in range(1, n+1):
    f=f*i
print(f/a)