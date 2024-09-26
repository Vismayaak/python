n=5
for i in range(n):
    for j in range(n-i):
        print("",end=" ")
    for j in range(i+1):
        if(j==0 or i==j or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()