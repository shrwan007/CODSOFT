import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

FILE_NAME = "tasks.json"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("650x450")
        self.root.configure(bg="#C7E2E2")

        self.tasks = self.load_tasks()

        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#d1eceb")
        style.configure("Treeview", font=("Arial", 11), rowheight=30)

        tree_frame = tk.Frame(root, bg="#8dc1bf")
        tree_frame.pack(pady=15, padx=15, fill="both", expand=True)

        self.tree = ttk.Treeview(tree_frame, columns=("Status", "Task Name", "Priority", "Deadline"), show='headings')

        self.tree.heading("Status", text="Status")
        self.tree.column("Status", width=60, anchor="center")

        self.tree.heading("Task Name", text="Task Name")
        self.tree.column("Task Name", width=250, anchor="w")

        self.tree.heading("Priority", text="Priority")
        self.tree.column("Priority", width=120, anchor="center")

        self.tree.heading("Deadline", text="Deadline")
        self.tree.column("Deadline", width=120, anchor="center")

        self.tree.pack(fill="both", expand=True)

        input_frame = tk.Frame(root, bg="#f4f9f9")
        input_frame.pack(pady=5)

        self.task_entry = tk.Entry(input_frame, width=25, font=("Arial", 11))
        self.task_entry.grid(row=0, column=0, padx=5)

        self.priority_combo = ttk.Combobox(input_frame, values=["High Priority", "Medium Priority", "Low Priority"], state="readonly", width=15, font=("Arial", 10))
        self.priority_combo.grid(row=0, column=1, padx=5)
        self.priority_combo.set("Medium Priority")

        self.deadline_entry = tk.Entry(input_frame, width=15, font=("Arial", 11))
        self.deadline_entry.grid(row=0, column=2, padx=5)
        self.deadline_entry.insert(0, "Due: Date")

        self.button_frame = tk.Frame(root, bg="#f4f9f9")
        self.button_frame.pack(pady=10)

        btn_bg = "#2a9d8f"
        btn_fg = "white"

        self.add_btn = tk.Button(self.button_frame, text="Add Task", bg=btn_bg, fg=btn_fg, font=("Arial", 10, "bold"), command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(self.button_frame, text="Mark Complete", bg=btn_bg, fg=btn_fg, font=("Arial", 10, "bold"), command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.edit_btn = tk.Button(self.button_frame, text="Edit Task", bg=btn_bg, fg=btn_fg, font=("Arial", 10, "bold"), command=self.edit_task)
        self.edit_btn.grid(row=0, column=2, padx=5)

        self.delete_btn = tk.Button(self.button_frame, text="Delete Task", bg="#d9dbda")
        self.delete_btn.grid(row=0, column=3, padx=5)

        self.refresh_list()

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(FILE_NAME, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def refresh_list(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        for index, task in enumerate(self.tasks):

            status = "☑" if task.get('completed') else "☐"
            name = task.get('name', 'Unnamed Task')
            priority = task.get('priority', 'Medium Priority')
            deadline = task.get('due_date', 'None')

            self.tree.insert("", tk.END, iid=index, values=(status, name, priority, deadline))

    def add_task(self):
        name = self.task_entry.get().strip()
        priority = self.priority_combo.get()
        deadline = self.deadline_entry.get().strip()

        if name and name != "Task description...":
            self.tasks.append({
                "name": name,
                "completed": False,
                "priority": priority,
                "due_date": deadline
            })
            self.save_tasks()
            self.refresh_list()

            self.task_entry.delete(0, tk.END)
            self.deadline_entry.delete(0, tk.END)
            self.deadline_entry.insert(0, "Due: Date")
        else:
            messagebox.showwarning("Warning", "Please enter a task name.")

    def complete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task from the list first.")
            return

        index = int(selected[0])
        self.tasks[index]['completed'] = True
        self.save_tasks()
        self.refresh_list()

    def edit_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task from the list first.")
            return

        index = int(selected[0])
        task = self.tasks[index]

        self.task_entry.delete(0, tk.END)
        self.task_entry.insert(0, task.get('name', ''))

        self.priority_combo.set(task.get('priority', 'Medium Priority'))

        self.deadline_entry.delete(0, tk.END)
        self.deadline_entry.insert(0, task.get('due_date', ''))

        self.tasks.pop(index)
        self.save_tasks()
        self.refresh_list()

    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a task from the list first.")
            return

        index = int(selected[0])
        self.tasks.pop(index)
        self.save_tasks()
        self.refresh_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()