a=input()
n=a.find('f')
nr=a.rfind('f')
if n!=nr:
    print(n)
    print(nr)
else:
    if n!=-1:
        print(n)