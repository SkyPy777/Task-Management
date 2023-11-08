
import datetime

# List to store the task of the user
my_list = []

print("\nOptions:")
print("\t1. Add Task")
print("\t2. View Task")
print("\t3. Mark as important")
print("\t4. Remove Task")
print("\t5. Quit")

while True:
    choose = input("\nEnter your option: ")

    if choose == "1":
        task = input("\nEnter task to add: ")
        is_important = input("Is this task important? (yes/no): ")== "yes"
        creation_date = datetime.date.today().strftime("%Y-%m-%d")
        my_list.append({
            "task": task,
            "important": is_important,
            "creation_date": creation_date,
            "completed": False
        })
        print(f"{task} added!")

    elif choose == "2":
        if not my_list:
            print("List is empty.")
        else:
            print("My List:")
            for index, task_data in enumerate(my_list, start=1):
                importance = "Important" if task_data["important"] else "Not Important"
                completion_status = "Completed" if task_data["completed"] else "Not Completed"
                print(f"{index}. {task_data['task']} \n-- {importance} \n-- Created on: {task_data['creation_date']} \n-- {completion_status}")

    elif choose == "3":
        if not my_list:
            print("List is empty.")
        else:
            task_number = int(input("Enter task number to mark as important: "))
            if 1 <= task_number <= len(my_list):
                my_list[task_number - 1]["important"] = True
                print(f"{my_list[task_number - 1]['task']} marked as important!")
            else:
                print("Enter a valid task number.")

    elif choose == "4":
        if not my_list:
            print("List is empty.")
        else:
            task_number = int(input("Enter task number to remove: "))
            if 1 <= task_number <= len(my_list):
                remove_task = my_list.pop(task_number - 1)
                print(f"{remove_task['task']} removed!")
            else:
                print("Enter a valid task number.")

    elif choose == "5":
        print("\nGoodbye!")
        break
    else:
        print("Enter a valid option.")
