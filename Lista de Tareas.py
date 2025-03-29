import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía")

def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)
        lista_tareas.delete(indice)
        lista_tareas.insert(indice, f"✔ {tarea}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada")

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar")

def agregar_con_enter(event):
    agregar_tarea()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# Campo de entrada
tk.Label(ventana, text="Nueva tarea:").pack(pady=5)
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=5)
entrada_tarea.bind("<Return>", agregar_con_enter)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Añadir Tarea", command=agregar_tarea).grid(row=0, column=0, padx=5)
tk.Button(frame_botones, text="Marcar como Completada", command=marcar_completada).grid(row=0, column=1, padx=5)
tk.Button(frame_botones, text="Eliminar Tarea", command=eliminar_tarea).grid(row=0, column=2, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=15)
lista_tareas.pack(pady=10)

ventana.mainloop()
