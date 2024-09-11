n=int(input("Enter the number:"))
temp=n
sum_of_num=0
length_of_digits=len(str(n))
while temp>0:
    digit=temp%10
    sum_of_num+=digit**length_of_digits
    temp//=10   
if sum_of_num==n:
    print("it is an amstrong number")
else:
    print("not an amstrong number")
