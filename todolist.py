import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(
            self.frame, width=50, height=10, selectmode=tk.SINGLE
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(
            self.frame, orient=tk.VERTICAL, command=self.task_listbox.yview
        )
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack(pady=20)

        self.task_entry = tk.Entry(self.entry_frame, width=50)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_button = tk.Button(
            self.entry_frame, text="Add Task", command=self.add_task
        )
        self.add_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(
            root, text="Delete Task", command=self.delete_task
        )
        self.delete_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
