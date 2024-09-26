def string(s):
    vowels="a,e,i,o,u,A,E,I,O,U"
    l=0
    r=len(s)-1
    s=list(s)
    while l<r:
        if s[l] not in vowels:
            l=l+1
            continue
        if s[r] not in vowels:
            r=r-1
            continue
        s[l],s[r]=s[r],s[l]
        l=l+1
        r=r-1
    return "".join(s)
s = input("Enter a string: ")
res = string(s)
print(res)