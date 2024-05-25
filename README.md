# ToDo List Application

## Overview

This project is a simple To-Do List application built using Python and the Tkinter library for the GUI. It allows users to add and delete tasks from a list, making it easy to keep track of tasks and organize daily activities.

## Features

- **Add Task**: Users can input a task in the text entry field and add it to the task list by clicking the "Add Task" button.
- **Delete Task**: Users can delete a selected task from the list by clicking the "Delete Task" button.
- **GUI**: The application features a graphical user interface (GUI) built with Tkinter.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/violawa/todolist-python
   ```
2. Navigate to the project directory:
   ```sh
   cd todolist-python
   ```

### Running the Application

Run the application using Python:
```sh
python todolist.py
```

## User Interface
<img src="https://github.com/violawa/todolist-python/blob/main/GUI.png">

## Usage

1. **Launch the Application**: Run the `todolist.py` script to open the To-Do List application window.
2. **Add a Task**: Type a task into the entry field at the bottom of the window and click the "Add Task" button. The task will appear in the list.
3. **Delete a Task**: Select a task from the list by clicking on it, then click the "Delete Task" button to remove it from the list.

## Code Structure

- `todolist.py`: The main script that contains the `ToDoApp` class which handles the GUI and functionality.

### `ToDoApp` Class

- **Attributes**:
  - `root`: The main window of the application.
  - `tasks`: A list to store tasks.
  - `frame`: A frame to hold the listbox and scrollbar.
  - `task_listbox`: A listbox widget to display tasks.
  - `scrollbar`: A scrollbar for the listbox.
  - `entry_frame`: A frame to hold the entry field and add button.
  - `task_entry`: An entry widget for task input.
  - `add_button`: A button to add tasks.
  - `delete_button`: A button to delete tasks.

- **Methods**:
  - `__init__`: Initializes the GUI components.
  - `add_task`: Adds a task to the list.
  - `delete_task`: Deletes a selected task from the list.
  - `update_task_listbox`: Updates the listbox to display the current list of tasks.
---

Happy task managing!
