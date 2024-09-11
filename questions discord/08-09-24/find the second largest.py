n=int(input("Enter the no of elements"))
a=[]
print("Enter the elements:")
for i in range(n):
    b=int(input())
    a.append(b)
for i in range(n):
    for j in range(i,n):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("second largest element is:",a[n-2])