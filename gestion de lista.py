import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

def mark_completed(event=None):
    try:
        selected_index = task_list.curselection()[0]
        task = task_list.get(selected_index)
        task_list.delete(selected_index)
        task_list.insert(selected_index, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcarla como completada.")

def delete_task(event=None):
    try:
        selected_index = task_list.curselection()[0]
        task_list.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminarla.")

def close_app(event=None):
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x300")

# Campo de entrada
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)  # Atajo para añadir tarea

# Botones
btn_add = tk.Button(root, text="Añadir Tarea", command=add_task)
btn_add.pack(pady=5)
btn_complete = tk.Button(root, text="Marcar Completada", command=mark_completed)
btn_complete.pack(pady=5)
btn_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
btn_delete.pack(pady=5)

# Lista de tareas
task_list = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
task_list.pack(pady=10)

# Asociar atajos de teclado
root.bind("<c>", mark_completed)
root.bind("<d>", delete_task)
root.bind("<Delete>", delete_task)
root.bind("<Escape>", close_app)

# Ejecutar la aplicación
root.mainloop()
