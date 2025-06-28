

current_tasks = []


def view_tasks(current_tasks):
    if len(current_tasks) == 0:
        print("there are no tasks")

    else:
        x = 0
        for task in current_tasks:
            print(f"{x}. {task}")
            x+=1



def add_task(current_tasks):
    new_task = input("enter a new task ")
    current_tasks.append(new_task)
    print(" the tasks are now")
    view_tasks(current_tasks)

def remove_task(current_tasks):
    while True:

        print("these are your items")
        view_tasks(current_tasks)

        remove = input("what would you like to remove ")

        if remove not in current_tasks:
            print("that is not a task")

        else:
            current_tasks.remove(remove)
            break

    print("Updated list")
    print("")
    view_tasks(current_tasks)




def menu():

    while True:
        print("""
        1. View Tasks
        2. Add a Task
        3. Remove a Task
        4. Exit
        """)

        choice = int(input("What is your choice "))
        if choice in [1, 2, 3, 4]:
            break
        else:
            print("Chosse  a correct option")

    if choice == 1:
        view_tasks(current_tasks)

    elif choice == 2:
        add_task(current_tasks)
    elif choice ==3:
        remove_task(current_tasks)

    elif choice == 4:
        print("Bye")
        exit()
while True:
    menu()
