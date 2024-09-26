task=[]
while True:
    print("Main Menu")
    print(" 1.ADD TASK\n 2.VIEW ALL TASK\n 3.UPDATE TASK\n 4.MARK TASK AS COMPLETED\n 5.DELETE TASK\n 6.SEARCH TASK BY NAME\n 7.EXIT\n")
    choice=int(input("Enter your choice:"))
    if choice==1:
        x=[]
        a=input("Enter the task name:")
        x.append(a)
        b=input("Enter the Description :")
        x.append(b)
        c=(input("Enter Due Date:"))
        x.append(c)
        d=input("Enter Priority level:")
        x.append(d)
        task.append(x)
        print("Task Added")
    elif choice==2:
        print(task)
    elif choice==3:
        e=input("Enter the task name to update:")
        for z in task:
            if z[0]==e:
                z[0]=input("Enter the new task name:")
                z[1]=input("Enter the new Description:")
                z[2]=input("Enter the new Due Date:")
                z[3]=input("Enter the  new Priority leve;:")
                print("Task updated")
                break
        else:
            print("Task not updated")
    elif choice==4:
        f=input("Enter task name mark as to completed:")
        for k in task:
            if k[0]==f:
                k.append("True")
                print("Task mark completed")
                break
            else:
                print("Task not found")
    elif choice==5:
            g=input("Enter the task ito delete:")
            for s in task:
                if s[0]==g:
                        task.remove(s)
                        print("Deleted Succsessfully")
                        break
                else:
                    print("Not deleted")
    elif choice==6:
        flag=0
        h=input("Enter task name to search:")
        for l in task:
            if l[0]==h:
                print("Task name:",l[0])
                print("Description:",l[1])
                print("Due Date:",l[2])
                print("Priority level",l[3])
                flag=1
                
            if flag==0:
                print("Not Found")

                
    elif choice==7:
        print("Exit")
        break
