students=[]
a=int(input("Enter the number of students:"))
id=0
for i in range(a):
    dict={"ID":"","Name":"","Age":"","marks":""}
    id=int(input("enter your id"))
    Name=input("Enter the name:")
    Age=input("Enter the age:")
    mark1=int(input("mark of subject 1:"))
    mark2=int(input("mark of subject 2:"))
    mark3=int(input("mark of subject 3:"))
    id=id+1
    dict["ID"]=id
    dict["Name"]=Name
    dict["Age"]=Age
    dict["marks"]=[mark1,mark2,mark3]
    students.append(dict)
print(students)