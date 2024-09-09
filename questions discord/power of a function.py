x=int(input("Enter a number:"))
y=int(input("enter the power number:"))
result=1

for i in range(y):
    result*=x
print(f"{x}^{y}={result}")