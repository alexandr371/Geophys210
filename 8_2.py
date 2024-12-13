def capitalize(a):
    string=[str(s) for s in a]
    string[0]=chr(ord(a[0])-32)
    for i in range(1, len(a)):
        if a[i-1]==' ':
            string[i]=chr(ord(a[i])-32)
    return ''.join(string)
print(capitalize(input()))