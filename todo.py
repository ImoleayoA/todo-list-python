# TODO-LIST APP - CiA
from datetime import datetime


# Create an empty list called TASKS
TASKS = []

# Create an empty list called TRASH
TRASH = []


# REPEAT
while True:
    try:
        main_menu = (

            "===== TO-DO LIST =====\n"
            "1. ADD TASK\n"
            "2. VIEW / EDIT TASK\n"
            "3. TRASH\n"
            "4. EXIT\n"
        )

        print(main_menu)

        option = input("Select an option or type 'exit' to end program: ").strip()

        # ADD TASK
        if option == "1":
            print("=========================\nADD TASK\n=========================")
            print("Task Name\nExample: Wash Clothes")

            # TASK NAME
            while True:
                taskName = input("Enter Task Name: ").strip()

                if not taskName:
                    print("Not valid")
                elif len(taskName) > 100:
                    print("Task name cannot be more than 100 characters")
                else:
                    break

            # STATUS
            while True:
                try:
                    print(
                        "SELECT STATUS\n"
                        "1. Pending\n"
                        "2. Ongoing\n"
                        "3. Completed"
                    )

                    status = int(input("Select an Option: ").strip())

                    if status == 1:
                        print("Pending Selected")
                        status = "Pending"
                    elif status == 2:
                        print("Ongoing Selected")
                        status = "Ongoing"
                    elif status == 3:
                        print("Completed Selected")
                        status = "Completed"
                    else:
                        print("Select a valid option")
                        continue

                    break

                except ValueError:
                    print("Enter a valid option")

            # PRIORITY
            while True:
                try:
                    print(
                        "SELECT PRIORITY\n"
                        "1. Low\n"
                        "2. Medium\n"
                        "3. High"
                    )

                    priority = int(input("Select an Option: ").strip())

                    if priority == 1:
                        print("Low Selected")
                        priority = "Low"
                    elif priority == 2:
                        print("Medium Selected")
                        priority = "Medium"
                    elif priority == 3:
                        print("High Selected")
                        priority = "High"
                    else:
                        print("Select a valid option")
                        continue

                    break

                except ValueError:
                    print("Select a valid option")

            # CATEGORY
            while True:
                try:
                    print(
                        "SELECT CATEGORY\n"
                        "1. School\n"
                        "2. Work\n"
                        "3. Personal\n"
                        "4. Other"
                    )

                    category = int(input("Select an Option: ").strip())

                    if category == 1:
                        print("School Selected")
                        category = "School"

                    elif category == 2:
                        print("Work Selected")
                        category = "Work"

                    elif category == 3:
                        print("Personal Selected")
                        category = "Personal"

                    elif category == 4:
                        print("Other Selected")

                        # CUSTOM CATEGORY
                        while True:
                            other = input("Enter Category: ").strip()

                            if not other:
                                print("Category cannot be empty. Please enter a category")
                            elif len(other) > 50:
                                print("Category cannot be more than 50 characters")
                            else:
                                category = other
                                break

                    else:
                        print("Enter a valid option")
                        continue

                    break

                except ValueError:
                    print("Enter a valid option")

            createdAt = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

            lastEdited = None

            task = {
                "Task Name": taskName,
                "Status": status,
                "Priority": priority,
                "Created At": createdAt,
                "Category": category,
                "Last Edited": lastEdited
            }

            # Add the task to TASKS
            TASKS.append(task)
            print("Task added successfully")

        # VIEW / EDIT TASK
        elif option == "2":

            if not TASKS:
                print("Task is Empty\n0. Back to Main Menu")

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

                    # DISPLAY TASKS
                    for number, task in enumerate(TASKS, start=1):
                        print(f"\nTask {number}")

                        for key, value in task.items():
                            if key == "Last Edited" and value is None:
                                continue

                            print(f"{key} : {value}")

                    print(
                        "\nSELECT AN OPTION (1/2/3)\n"
                        "1. Edit\n"
                        "2. Delete\n"
                        "3. Back to Main Menu"
                    )

                    try:
                        action = int(input("Enter your choice: ").strip())

                        # EDIT
                        if action == 1:
                            print("Select which task to edit\n")

                            back_to_view_edit = False

                            while True:
                                for number, task in enumerate(TASKS, start=1):
                                    print(f"Task {number}: {task['Task Name']}")

                                print("0. Back to View / Edit")

                                try:
                                    selection = int(
                                        input("Enter Task Number: ").strip())

                                    if selection == 0:
                                        break

                                    if (selection < 1 or selection > len(TASKS)):
                                        print(
                                            "Please select a valid task number")
                                        continue

                                    selected_task = TASKS[selection - 1]

                                    print(f"\nTask {selected_task['Task Name']}")

                                    # EDIT MENU
                                    while True:
                                        print("\nWhat would you like to edit?")
                                        print(
                                            "1. Task Name\n"
                                            "2. Status\n"
                                            "3. Priority\n"
                                            "4. Category\n"
                                            "5. Back to Previous Menu\n"
                                            "6. Back to View / Edit"
                                        )

                                        try:
                                            edit_choice = int(input("Enter your choice: ").strip())

                                            # EDIT TASK NAME
                                            if edit_choice == 1:
                                                while True:
                                                    new_task_name = input("Enter new Task Name: ").strip()

                                                    if not new_task_name:
                                                        print("Please enter a valid task name")

                                                    elif len(new_task_name) > 100:
                                                        print("Task name cannot be more than 100 characters")

                                                    elif (selected_task["Task Name"]== new_task_name):
                                                        print(f"Task Name is alreadyc'{new_task_name}'")
                                                        break

                                                    else:
                                                        selected_task["Task Name"] = new_task_name
                                                        selected_task["Last Edited"] = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")
                                                        print("Task Name updated successfully")
                                                        print(f"New Task Name: {selected_task['Task Name']}")
                                                        break

                                            # EDIT STATUS
                                            elif edit_choice == 2:

                                                while True:
                                                    try:
                                                        print(
                                                            "\nSELECT STATUS\n"
                                                            "1. Pending\n"
                                                            "2. Ongoing\n"
                                                            "3. Completed"
                                                        )

                                                        new_status = int(
                                                            input("Select an option: ").strip())

                                                        if new_status == 1:
                                                            new_status = "Pending"

                                                        elif new_status == 2:
                                                            new_status = "Ongoing"

                                                        elif new_status == 3:
                                                            new_status = "Completed"
                                                        else:
                                                            print("Select a valid option")
                                                            continue

                                                        if selected_task["Status"] == new_status:
                                                            print(f"Status is already {new_status}")
                                                        else:
                                                            selected_task["Status"] = new_status

                                                            selected_task["Last Edited"] = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

                                                            print("Status updated successfully")

                                                        print(f"New Status: {selected_task['Status']}")
                                                        break

                                                    except ValueError:
                                                        print("Enter a valid option")
                                                break

                                            # EDIT PRIORITY
                                            elif edit_choice == 3:
                                                print("Edit Priority")

                                                while True:
                                                    try:
                                                        print(
                                                            "\nSELECT PRIORITY\n"
                                                            "1. Low\n"
                                                            "2. Medium\n"
                                                            "3. High"
                                                        )

                                                        new_priority = int(input("Select an option: ").strip())

                                                        if new_priority == 1:
                                                            new_priority = "Low"

                                                        elif new_priority == 2:
                                                            new_priority = "Medium"

                                                        elif new_priority == 3:
                                                            new_priority = "High"

                                                        else:
                                                            print("Select a valid option")
                                                            continue

                                                        if selected_task["Priority"]== new_priority:
                                                            print(f"Priority is already {new_priority}")
                                                        else:
                                                            selected_task["Priority"] = new_priority

                                                            selected_task["Last Edited"] = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

                                                            print(
                                                                "Priority updated successfully")

                                                        print(f"New Priority: {selected_task['Priority']}")
                                                        break

                                                    except ValueError:
                                                        print("Enter a valid option")
                                                break

                                            # EDIT CATEGORY
                                            elif edit_choice == 4:

                                                while True:
                                                    try:
                                                        print(
                                                            "\nSELECT CATEGORY\n"
                                                            "1. School\n"
                                                            "2. Work\n"
                                                            "3. Personal\n"
                                                            "4. Other\n"
                                                            "5. Back to Previous Menu"
                                                        )

                                                        new_category = int(input("Select an option: ").strip())

                                                        if new_category == 1:
                                                            new_category = "School"

                                                        elif new_category == 2:
                                                            new_category = "Work"

                                                        elif new_category == 3:
                                                            new_category = "Personal"

                                                        elif new_category == 4:

                                                            while True:
                                                                other = input("Enter New Category: ").strip()

                                                                if not other:
                                                                    print("Category cannot be empty. Please enter a category")

                                                                elif len(other) > 50:
                                                                    print("Category cannot be more than 50 characters")

                                                                elif selected_task["Category"]== other:
                                                                    print(f"Category is already '{other}'")

                                                                else:
                                                                    selected_task["Category"] = other

                                                                    selected_task["Last Edited"] = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

                                                                    print("Category updated successfully")

                                                                    print(f"New Category: {selected_task['Category']}")
                                                                    break
                                                            break

                                                        elif new_category == 5:
                                                            break

                                                        else:
                                                            print("Select a valid option")
                                                            continue

                                                        # This handles
                                                        # School / Work /
                                                        # Personal
                                                        if new_category in ("School", "Work", "Personal"):
                                                            if selected_task["Category"]== new_category:
                                                                print(f"Category is already {new_category}")
                                                            else:
                                                                selected_task["Category"] = new_category

                                                                selected_task["Last Edited"] = datetime.now().strftime("%A, %B %d, %Y %I:%M %p" )

                                                                print("Category updated successfully")

                                                            print(f"New Category: {selected_task['Category']}")
                                                        break

                                                    except ValueError:
                                                        print("Enter a valid option")

                                            # BACK TO PREVIOUS MENU
                                            elif edit_choice == 5:
                                                break

                                            # BACK TO VIEW / EDIT
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

                        # DELETE
                        elif action == 2:
                            print("Select which task to delete:\n")

                            back_to_main = False

                            while True:
                                for number, task in enumerate(TASKS, start=1):
                                    print(f"Task {number}: "{task['Task Name']}")

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
                                        confirm = input("Are you sure you want to move this task to Trash? Y/N or Yes/No: ").strip().lower()

                                        if confirm in ("y", "yes"):
                                            deleted_task = TASKS.pop(selection - 1)

                                            TRASH.append(deleted_task)

                                            print("Task moved to Trash successfully")

                                            if not TASKS:
                                                print("Task is Empty\n 0. Back to Main Menu")

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

                                        elif confirm in ("n", "no"):
                                            print("Delete Cancelled")
                                            break

                                        else:
                                            print("Please enter Y/N or Yes/No")

                                    if back_to_main:
                                        break

                                except ValueError:
                                    print("Please select a valid task Number")

                            if back_to_main:
                                break

                        # BACK TO MAIN MENU
                        elif action == 3:
                            print("\n")
                            break

                        else:
                            print("Invalid option")

                    except ValueError:
                        print("Invalid option")

        # TRASH
        elif option == "3":

            if not TRASH:
                print("Trash is empty\n0. Back to Main Menu")

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
                        print(
                            "\n1. Restore\n"
                            "2. Permanently Delete\n"
                            "3. Back to Main Menu"
                        )

                        selection = int(input("Select an option: ").strip())

                        # RESTORE
                        if selection == 1:

                            while True:
                                print("\nSelect which task to restore:")

                                for number, task in enumerate(TRASH, start=1):
                                    print( f"{number}. {task['Task Name']}")

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

                        # PERMANENT DELETE
                        elif selection == 2:
                            print("Permanently Delete selected")

                            for number, task in enumerate(TRASH, start=1):
                                print(f"{number}. {task['Task Name']}")

                            print("0. Back")

                            try:
                                delete_selection = int(
                                    input("Enter task number: ").strip())

                                if delete_selection == 0:
                                    continue

                                if delete_selection < 1 or delete_selection > len(TRASH):
                                    print("Select a valid task number")
                                    continue

                                selected_task = TRASH[delete_selection - 1]

                                print(f"\nTask:{selected_task['Task Name']}")

                                while True:
                                    confirm = input("Are you sure you want to delete this task? Y/N or Yes/No: ").strip().lower()

                                    if confirm in ("y", "yes"):
                                        deleted_task = TRASH.pop(delete_selection - 1)

                                        print(f"Task '{deleted_task['Task Name']}' permanently deleted")

                                        break

                                    elif confirm in ("n", "no"):
                                        print("Delete cancelled")
                                        break

                                    else:
                                        print("Please enter Y/N or Yes/No")

                            except ValueError:
                                print("Enter a valid task number")

                        # BACK TO MAIN MENU
                        elif selection == 3:
                            break

                        else:
                            print("Select a valid option")

                    except ValueError:
                        print("Invalid option")

        # EXIT
        elif option == "4" or option.lower() == "exit":
            print("Exiting The To-Do List...")
            break

        else:
            print("Invalid option")

    # CTRL+C / CTRL+D
    except (KeyboardInterrupt, EOFError):
        print("Exiting the To-Do List...")
        break