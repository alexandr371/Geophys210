ax=int(input())
ay=int(input())
bx=int(input())
by=int(input())
if ax==bx and ay==by:
    print("NO")
else: 
    if abs(ax-bx)<=1 and abs(ay-by)<=1:
        print("YES")
    else:
        print("NO")