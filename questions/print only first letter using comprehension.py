num=[]
a=int(input("Enter the size:"))
for i in range(a):
    b=input("Enter the strings:")
    num.append(b)
print(num)
num=[b[0] for b in num]
print(num)
