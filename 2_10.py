ax=int(input())
ay=int(input())
bx=int(input())
by=int(input())
if abs(ax-bx)==abs(ay-by) or ax==bx or ay==by:
    print("YES")
else:
    print("NO")