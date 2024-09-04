dictionary1={}
a=int(input("Enter the size: "))
for i in range(a):

    dictionary2={}
    name = input("enter your name : ")
    age = input("enter your age: ")
    city =input("enter your city")
    dictionary2["name"]=name
    dictionary2["age"]=age
    dictionary2["city"]=city
    dictionary1[i+1]=dictionary2

