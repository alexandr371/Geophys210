k=int()
a=input()
i1=a.find('f')
a=a.replace('f', '', 1)
i2=a.find('f')
if i1==-1:
    print(-2)
else:
    print(i2)