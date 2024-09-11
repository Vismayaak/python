n=5
for i in range(n):
    for j in range(n):
        if(j==0 or j==n-1):
            print("*",end=" ")
        elif(i==0 or i==4 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()