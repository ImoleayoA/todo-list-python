# CiA To-Do List App

A simple command-line To-Do List application built with Python.
The app allows users to create, view, edit, delete, restore, and permanently delete tasks directly from the terminal.

## Features

* Add new tasks
* View all tasks
* Edit existing tasks
* Move tasks to Trash
* Restore deleted tasks
* Permanently delete tasks

* Set task status
  * Pending
  * Ongoing
  * Completed
  
* Set task priority
  * Low
  * Medium
  * High
  
* Assign task categories
  * School
  * Work
  * Personal
  * Other
  
* Track when a task was created
* Track when a task was last edited
* Input validation for task information
* Supports exiting by selecting `4` or typing `exit`
* Handles `Ctrl+C` and `Ctrl+D` gracefully

## Built With

* Python 3
* Python `datetime` module

## Task Information

Each task contains:

| Field       | Description                              |
| ----------- | ---------------------------------------- |
| Task Name   | The name of the task                     |
| Status      | Pending, Ongoing, or Completed           |
| Priority    | Low, Medium, or High                     |
| Category    | School, Work, Personal, or Other         |
| Created At  | Date and time the task was created       |
| Last Edited | Date and time the task was last modified |

## Getting Started

### Prerequisites

You need Python 3 installed on your computer.

Check whether Python is installed:

```bash
python3 --version
```

### Installation

Clone the repository:

```bash
git clone https://github.com/Imoleayo98/todo-list-python.git
```

Move into the project directory:

```bash
cd todo-list-python
```

### Running the Application

Run the program with:

```bash
python3 todo.py
```

You should see:

```text
===== TO-DO LIST =====
1. ADD TASK
2. VIEW / EDIT TASK
3. TRASH
4. EXIT
```

## How to Use

### 1. Add a Task

Select:

```text
1. ADD TASK
```

You will be asked to enter:

* Task name
* Status
* Priority
* Category

The application automatically records the creation date and time.

### 2. View / Edit Tasks

Select:

```text
2. VIEW / EDIT TASK
```

You can:

* View your tasks
* Edit a task name
* Change status
* Change priority
* Change category
* Move a task to Trash

### 3. Trash

Select:

```text
3. TRASH
```

From the Trash menu you can:

* Restore a task
* Permanently delete a task
* Return to the main menu

Restored tasks retain their existing task information.

### 4. Exit

You can exit by selecting:

```text
4. EXIT
```

or typing:

```text
exit
```

The application also handles `Ctrl+C` and `Ctrl+D` without crashing.

## Project Structure

```text
todo-list-python/
│
├── todo.py
├── .gitignore
└── README.md
```

## Project Purpose

This project was created as a Python learning project to practice:

* Variables
* Lists
* Dictionaries
* Loops
* Conditional statements
* `try/except`
* User input and validation
* Functions/modules from the Python standard library
* Working with dates and times
* Managing application state
* Git and GitHub

## Future Improvements

Possible improvements for future versions include:

* Save tasks to a file or database
* Add task due dates
* Add search and filtering
* Sort tasks by priority or status
* Add recurring tasks
* Create a graphical user interface


## Author

Imoleayo98

GitHub:
https://github.com/ImoleayoA

## License

This project is currently available for personal and educational use.
