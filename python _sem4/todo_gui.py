import tkinter as tk
from tkinter import messagebox

# Main app window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Task list
tasks = []

# Function to update listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Add task
def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty")

# Delete task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except:
        messagebox.showwarning("Selection Error", "No task selected")

# Widgets
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=10)
listbox.pack(pady=10)

root.mainloop()
