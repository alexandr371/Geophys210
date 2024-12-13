a=[int(s) for s in input().split()]

for i in range(1, len(a), 2):
    a[i], a[i-1]=str(a[i-1]), str(a[i])
a[-1]=str(a[-1])
print(' '.join(a))