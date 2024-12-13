ans='NO'
a=[]
for i in range(8):
    a.append([int(j) for j in input().split()])
for i in range(8):
    for j in range(i+1, 8):
        if abs(a[i][0]-a[j][0]==a[i][1]-a[j][1]) or a[i][0]==a[j][0] or a[i][1]==a[j][1]:
            ans='YES'
            break
print(ans)