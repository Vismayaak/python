l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    b=int(input("Enter the element: "))
    l.append(b)
unique=[]
for i in range(n):
    flag=0
    for j in range(n):
        if(l[i]==l[j]and i!=j):
            flag=1        
    if(flag==0):
        unique.append(l[i])
print(unique)
count=len(unique)
if(count==0):
    print("null")
else:
    b=unique[0]
    for i in range(count):
        if(b<unique[i]):
            b=unique[i]
    print("largest element ",b)