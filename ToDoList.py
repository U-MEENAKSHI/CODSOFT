import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []
        self.load_tasks()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(root, width=52)
        self.entry.pack(pady=10)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.complete_task_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to complete.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            display_text = f"[{'✓' if task['completed'] else ' '}] {task['task']}"
            self.task_listbox.insert(tk.END, display_text)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)
        messagebox.showinfo("Info", "Tasks saved successfully!")

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
            self.update_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
