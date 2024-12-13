a=input()
ans=str()
for i in range(len(a)+1):
    ans=ans+a[i] if i%3!=0 else ans
print(ans)