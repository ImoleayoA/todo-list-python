#TODO-LIST APP - CiA
from datetime import datetime

#Create an empty list called TASKS
TASKS = []
#Create an empty list called TRASH
TRASH = []

#REPEAT
while True:
    try:
        main_menu = ("===== TO-DO LIST =====\n"
    
            "1. ADD TASK\n"
            "2. VIEW / EDIT TASK\n"
            "3. TRASH\n"
            "4. EXIT\n")

        print(main_menu)
        option = input("Select an option or type 'exit' to end program: ").strip()
        if option == "1":
            print("=========================\nADD TASK\n=========================")
            print("Task Name\nExample: Wash Clothes")

            while True:
                taskName = input("Enter Task Name: ").strip()
                if not taskName:
                    print("Not valid")
                elif len(taskName) > 100:
                    print("Task name cannot be more than 100 characters")
                else:
                    break

            while True:
                try:
                    print("SELECT STATUS\n1. Pending\n2. Ongoing\n3. Completed")
                    status = int(input("Select an Option: ").strip())
                    if status == 1:
                        print("Pending Selected")
                        status = "Pending"
                        break
                    elif status == 2:
                        print("Ongoing Selected")
                        status = "Ongoing"
                        break
                    elif status == 3:
                        print("Completed Selected")
                        status = "Completed"
                        break
                    else:
                        print("Select a valid option")
                except ValueError:
                    print("Enter a valid option")
            while True:
                try:
                    print("SELECT PRIORITY\n1.Low\n2.Medium\n3.High")
                    priority = int(input("Select an Option: ").strip())
                    if priority == 1:
                        print("Low Selected")
                        priority = "Low"
                        break
                    elif priority == 2:
                        print("Medium Selected")
                        priority = "Medium"
                        break
                    elif priority == 3:
                        print("High Selected")
                        priority = "High"
                        break
                    else:
                        print("Select a valid option")
                except ValueError:
                    print("Select a valid option")
            while True:
                try:
                    print("SELECT CATEGORY\n1.School\n2.Work\n3.Personal\n4.Other")
                    category = int(input("Select an Option: ").strip())
                    if category == 1:
                        print("School Selected")
                        category = "School"
                        break
                    elif category == 2:
                        print("Work Selected")
                        category = "Work"
                        break
                    elif category == 3:
                        print("Personal Selected")
                        category = "Personal"
                        break
                    elif category == 4:
                        print("Other Selected")
                        category = "Other"
                        break
                    else:
                        print("Enter a valid option")
                except ValueError:
                    print("Enter a valid option")

            createdAt = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")
            lastEdited = None

            task = {"Task Name": taskName,
                    "Status": status,
                    "Priority": priority,
                    "Created At": createdAt,
                    "Category": category,
                    "Last Edited": lastEdited}

            #Add the task to TASKS
            TASKS.append(task)
            print("Task added successfully")

        elif option == "2":
            if not TASKS:
                print("Task is Empty\n0.Back to Main Menu")
                while True:
                    try:
                        main = int(input("Enter 0: ").strip())
                        if main == 0:
                            print("Main Menu Selected")
                            break
                        else:
                            print(f"{main} is not a valid option")
                    except ValueError:
                        print("Invalid option")
            else:
                while True:
                    for number, task in enumerate(TASKS, start=1):
                        print(f"\nTask {number}")
                        for key, value in task.items():
                            if key == "Last Edited" and value is None:
                                continue
                            print(f"{key} : {value}")

                    print("\nSELECT AN OPTION (1/2/3) \n1.Edit\n2.Delete\n3.Back to Main Menu")
                    try:
                        action = int(input("Enter your choice: ").strip())
                        if action == 1:
                            print("Select which task to edit\n")
                            back_to_view_edit = False
                            while True:
                                for number, task in enumerate(TASKS, start=1):
                                    print(f"Task {number}: {task['Task Name']}")
                                print("0. Back to View / Edit")
                                try:
                                    selection = int(input("Enter Task Number: ").strip())
                                    if selection == 0:
                                        break
                                    if selection < 1 or selection > len(TASKS):
                                        print("Please select a valid task number")
                                        continue
                                    selected_task = TASKS[selection - 1]
                                    print(f"\nTask {selected_task['Task Name']}")
                                    while True:
                                        print("\n What would you like to edit?")
                                        print("1. Task Name")
                                        print("2. Status")
                                        print("3. Priority")
                                        print("4. Category")
                                        print("5. Back to Previous Menu")
                                        print("6. Back to View / Edit")

                                        try:
                                            edit_choice = int(input("Enter your choice: ").strip())
                                            if edit_choice == 1:
                                               while True:
                                                   new_task_name = input("Enter new Task Name: ").strip()
                                                   if not new_task_name:
                                                       print("Please enter a valid task name")
                                                   elif len(new_task_name) > 100:
                                                       print("Task name cannot be more than 100 characters")
                                                   elif selected_task["Task Name"] == new_task_name:
                                                       print(f"Task Name is already '{new_task_name}'")
                                                       break
                                                   else:
                                                       selected_task["Task Name"] = new_task_name
                                                       selected_task["Last Edited"] = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")
                                                       print("Task Name updated successfully")
                                                       print(f"New Task Name: {selected_task['Task Name']}")
                                                       break
                                            elif edit_choice == 2:
                                                while True:
                                                    try:
                                                        print("\nSELECT STATUS\n1.Pending\n2.Ongoing\n3.Completed")
                                                        new_status = int(input("Select an option: ").strip())
                                                        if new_status == 1:
                                                            if selected_task["Status"] == "Pending":
                                                                print("Status is already Pending")
                                                                break
                                                            else:
                                                                selected_task["Status"] = "Pending"
                                                                selected_task["Last Edited"] = datetime.now().strftime("%A, %B, %d, %Y %I:%M %p")
                                                            break
                                                        elif new_status == 2:
                                                            if selected_task["Status"] == "Ongoing":
                                                                print("Status is already Ongoing")
                                                                break
                                                            else:
                                                                selected_task["Status"] = "Ongoing"
                                                                selected_task["Last Edited"] = datetime.now().strftime(
                                                                    "%A, %B %d, %Y %I:%M %p")
                                                            break
                                                        elif new_status == 3:
                                                            if selected_task["Status"] == "Completed":
                                                                print("Status is already Completed")
                                                                break
                                                            else:
                                                                selected_task["Status"] = "Completed"
                                                                selected_task["Last Edited"] = datetime.now().strftime(
                                                                    "%A, %B %d, %Y %I:%M %p")
                                                            break
                                                        else:
                                                            print("Select a valid option")
                                                    except ValueError:
                                                        print("Enter a valid option")

                                                print("Status updated successfully")
                                                print(f"New Status: {selected_task['Status']}")
                                                break

                                            elif edit_choice == 3:
                                                print("Edit Priority")
                                                while True:
                                                    try:
                                                        print("\nSELECT PRIORITY\n1.Low\n2.Medium\n3.High")
                                                        new_priority = int(input("Select an option: ").strip())
                                                        if new_priority == 1:
                                                            if selected_task["Priority"] == "Low":
                                                                print("Priority is already Low")
                                                                break
                                                            else:
                                                                selected_task["Priority"] = "Low"
                                                                selected_task["Last Edited"] = datetime.now().strftime(
                                                                    "%A, %B %d, %Y %I:%M %p")
                                                            break
                                                        elif new_priority == 2:
                                                            if selected_task["Priority"] == "Medium":
                                                                print("Priority is already Medium")
                                                                break
                                                            else:
                                                                selected_task["Priority"] = "Medium"
                                                                selected_task["Last Edited"] = datetime.now().strftime(
                                                                    "%A, %B %d, %Y %I:%M %p")
                                                            break
                                                        elif new_priority == 3:
                                                            if selected_task["Priority"] == "High":
                                                                print("Priority is already High")
                                                                break
                                                            else:
                                                                selected_task["Priority"] = "High"
                                                                selected_task["Last Edited"] = datetime.now().strftime(
                                                                    "%A, %B %d, %Y %I:%M %p")
                                                            break
                                                        else:
                                                            print("Select a valid option")
                                                    except ValueError:
                                                        print("Enter a valid option")

                                                print("Priority updated successfully")
                                                print(f"New Priority: {selected_task['Priority']}")
                                                break

                                            elif edit_choice == 4:
                                                while True:
                                                    try:
                                                        print("\nSELECT CATEGORY\n1.School\n2.Work\n3.Personal\n4.Other\n5.Back to Previous Menu")
                                                        new_category = int(input("Select an option: ").strip())
                                                        if new_category == 1:
                                                            if selected_task["Category"] == "School":
                                                                print("Category is already School")
                                                                break
                                                            else:
                                                                selected_task["Category"] = "School"
                                                                selected_task["Last Edited"] = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")
                                                            break
                                                        elif new_category == 2:
                                                            if selected_task["Category"] == "Work":
                                                                print("Category is already Work")
                                                                break
                                                            else:
                                                                selected_task["Category"] = "Work"
                                                                selected_task["Last Edited"] = datetime.now().strftime(
                                                                    "%A, %B %d, %Y %I:%M %p")
                                                            break
                                                        elif new_category == 3:
                                                            if selected_task["Category"] == "Personal":
                                                                print("Category is already Personal")
                                                                break
                                                            else:
                                                                selected_task["Category"] = "Personal"
                                                                selected_task["Last Edited"] = datetime.now().strftime(
                                                                    "%A, %B %d, %Y %I:%M %p")
                                                            break
                                                        elif new_category == 4:
                                                            while True:
                                                                other = input("Enter New Category: ").strip()
                                                                if not other:
                                                                    print("Category cannot be empty. Please enter a category")
                                                                elif len(other) > 50:
                                                                    print("Category cannot be more than 50 characters")
                                                                elif selected_task['Category'] == other:
                                                                    print(f"Category is already '{other}'")
                                                                else:
                                                                    selected_task["Category"] = other
                                                                    selected_task["Last Edited"] = datetime.now().strftime(
                                                                        "%A, %B %d, %Y %I:%M %p")
                                                                    print("Category updated successfully")
                                                                    print(f"New Category: {selected_task['Category']}")
                                                                    break
                                                            break
                                                        elif new_category == 5:
                                                            break
                                                        else:
                                                            print("Select a valid option")
                                                    except ValueError:
                                                        print("Enter a valid option")
                                            elif edit_choice == 5:
                                                break
                                            elif edit_choice == 6:
                                                back_to_view_edit = True
                                                break
                                            else:
                                                print("Invalid option")
                                        except ValueError:
                                            print("Please select a valid number")
                                    if back_to_view_edit:
                                        break
                                except ValueError:
                                    print("Please enter a valid option")

                        elif action == 2:
                            print("Select which task to delete:\n")

                            back_to_main = False

                            while True:
                                for number, task in enumerate(TASKS, start=1):
                                    print(f"Task {number}: {task['Task Name']}")

                                print("0. Back to View / Edit")
                                try:
                                    selection = int(input("Enter Task Number Of The Task You Want To Delete: ").strip())
                                    if selection == 0:
                                        break
                                    if selection < 1 or selection > len(TASKS):
                                        print("Select a valid task number")
                                        continue
                                    selected_task = TASKS[selection - 1]
                                    print(f"\nTask {selected_task['Task Name']}")
                                    for key, value in selected_task.items():
                                        if key == "Last Edited" and value is None:
                                            continue
                                        print(f"{key} : {value}")

                                    while True:
                                        confirm = input("Are you sure you want to move this task to Trash? Y/N or Yes/No").strip().lower()
                                        if confirm in ("y", "yes"):
                                            deleted_task = TASKS.pop(selection - 1)
                                            TRASH.append(deleted_task)
                                            print("Task moved to Trash successfully")

                                            if not TASKS:
                                                print("Task is Empty\n0.Back to Main Menu")
                                                while True:
                                                    try:
                                                        main = int(input("Enter 0: ").strip())
                                                        if main == 0:
                                                            back_to_main = True
                                                            break
                                                        else:
                                                            print(f"{main} is not a valid option")
                                                    except ValueError:
                                                        print("Invalid option")
                                                break
                                            break
                                        elif confirm in ("n", "no"):
                                            print("Delete Cancelled")
                                            break
                                        else:
                                            print("Please enter Y/N or Yes/No")
                                except ValueError:
                                    print("Please select a valid task Number")
                                if back_to_main:
                                    break
                            if back_to_main:
                                break
                        elif action == 3:
                            print("\n")
                            break
                        else:
                            print("Invalid option")

                    except ValueError:
                        print("Invalid option")
        elif option == "3":
            if not TRASH:
                print("Trash is empty\n0.Back to Main Menu")
                while True:
                    try:
                        main = int(input("Enter 0: ").strip())
                        if main == 0:
                            break
                        else:
                            print(f"{main} is not a valid option")
                    except ValueError:
                        print("Invalid option")
                continue
            else:
                while True:
                    if not TRASH:
                        print("Trash is Empty")
                        break

                    print("\n===== TRASH =====")
                    for number, task in enumerate(TRASH, start=1):
                        print(f"Task {number}: {task['Task Name']}")

                    try:
                        print("\n1.Restore\n2.Permanently Delete\n3.Back to Main Menu")
                        selection = int(input("Select an option: ").strip())
                        if selection == 1:
                            while True:
                                print("\nSelect which task to restore:")

                                for number, task in enumerate(TRASH, start=1):
                                    print(f"{number}. {task['Task Name']}")

                                print("0. Back")

                                try:
                                    restore_selection = int(input("Enter task number: ").strip())
                                    if restore_selection == 0:
                                        break

                                    if restore_selection < 1 or restore_selection > len(TRASH):
                                        print("Select a valid task number")
                                        continue

                                    restored_task = TRASH.pop(restore_selection - 1)
                                    TASKS.append(restored_task)

                                    print("Task restored successfully")
                                    print(f"Task Name: {restored_task['Task Name']}")
                                    break
                                except ValueError:
                                    print("Enter a valid task number")

                        elif selection == 2:
                            print("Permanently Delete selected")

                            for number, task in enumerate(TRASH, start=1):
                                print(f"{number}. {task['Task Name']}")
                            print("0. Back")

                            try:
                                delete_selection = int(input("Enter task number: ").strip())

                                if delete_selection == 0:
                                    break
                                if delete_selection < 1 or delete_selection > len(TRASH):
                                    print("Select a valid task number")
                                    continue

                                selected_task = TRASH[delete_selection - 1]
                                print(f"\nTask: {selected_task['Task Name']}")

                                while True:
                                    confirm = input("Are you sure you want to delete this task? Y/N or Yes/No").strip().lower()
                                    if confirm in ("y", "yes"):
                                        deleted_task = TRASH.pop(delete_selection - 1)
                                        print(f"task '{deleted_task['Task Name']}' permanently deleted")
                                        break
                                    elif confirm in ("n", "no"):
                                        print("Delete cancelled")
                                        break
                                    else:
                                        print("Please enter Y/N or Yes/No")
                                break
                            except ValueError:
                                print("Enter a valid task number")

                        elif selection == 3:
                            break
                        else:
                            print("select a valid option")
                    except ValueError:
                        print("Invalid option")

        elif option == "4" or option.lower() == "exit":
            print("Exiting The To-Do List...")
            break
        else:
            print("Invalid option")

    except (KeyboardInterrupt, EOFError):
        print("Exiting the To-Do List...")
        break