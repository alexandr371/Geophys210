a=input()
i1=a.find('h')
i2=a.rfind('h')
sub=str()
for s in range(i1+1, i2):
    sub=a[s]+sub
ans=a[:i1+1]+sub+a[i2:]
print(ans)