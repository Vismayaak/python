a=[]
n=int(input("enter the no of elements:"))
for i in range(n):
    b=int(input("enter the elements:"))
    a.append(b)
unique=[]
for i in range(n):
    value=0
    for j in range(n):
        if(a[i]==a[j]and i!=j):
            value=1
    if(value==0):
        unique.append(a[i])
print(unique)
count=len(unique)
if(count==0):
    print("null")
else:
    b=unique[0]
    for i in range(count):
        if(b<unique[i]):
            b=unique[i]
print("largest number",b)