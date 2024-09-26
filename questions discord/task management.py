tasks = []
while True:
    print("Main Menu:")
    print("1.Add Task")
    print("2.View All Tasks")
    print("3.Update Task")
    print("4.Mark Task as Completed")
    print("5.Delete Task")
    print("6.Search Task by Name")
    print("7.Exit")
    choice = input("Enter your choice: ")

    if choice =='1':
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        task_due_date = input("Enter task due date: ")
        task_priority = input("Enter task priority: ")
        task = {'name': task_name,'description': task_description,'due_date': task_due_date,'priority': task_priority,'completed': 'False'}
        print(task)
        tasks.append(task)
        print("Task added ")
    elif choice == '2':
        for task in tasks:
            print("Name:", task['name'])
            print("Description:", task['description'])
            print("Due Date:", task['due_date'])
            print("Priority:", task['priority'])
            print("Completed:", task['completed'])
    elif choice == '3':
        search_name = input("Enter the task  to update: ")
      
        for task in tasks:
            if task['name']== search_name:
            
                task['name'] = input("Enter new task name: ")
                task['description'] = input("Enter new task description: ")
                task['due_date'] = input("Enter new task due date: ")
                task['priority'] = input("Enter new task priority")
                print("Task updated ")
                break
        if not task_found:
            print("Task not found")
    elif choice =='4':
        search_name = input("Enter the task name to mark as completed: ")
        task_found=False
        for task in tasks:
            if task['Name']== search_name:
                task_found=True
                task['completed']=True
                print("Task marked as completed.")
                break
            if not task_found:
                print("Task not found.")
    elif choice == '5':
        search_name = input("Enter the name of the task  to delete: ")
        task_found = False
        for task in tasks:
            if task['Name'] ==search_name:
                task_found = True
                tasks.remove(task)
                print("Task deleted ")
                break
        if not task_found:
            print("Task not found")
    elif choice =='6':
        search_name = input("Enter the task name to search: ")
        task_found = False
        for task in tasks:
            if task['name'] == search_name:
                task_found = True
                print("Name:", task['name'])
                print("Description:", task['description'])
                print("Due Date:", task['due_date'])
                print("Priority:", task['priority'])
                print("Completed:",task['completed'])
                break
        if not task_found:
            print("Task not found.")
    else:
        if choice=='7':
            print("Exiting the program.")
            break
        else:
            print("invalid choice :")