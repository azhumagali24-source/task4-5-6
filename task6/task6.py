import tkinter as tk
from tkinter import messagebox

def calculate():
    name = name_entry.get()
    age = age_entry.get()
    if name == "" or age == "":
        messagebox.showerror("Ошибка", "Заполните все поля")
        return
    try:
        age = int(age)
    except:
        messagebox.showerror("Ошибка", "Возраст должен быть числом")
        return
    result_label.config(text=f"{name}, вам {age} лет")

root = tk.Tk()
root.title("Форма")

tk.Label(root, text="Имя:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Возраст:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Button(root, text="Показать", command=calculate).pack(pady=5)
result_label = tk.Label(root, text="Результат:")
result_label.pack()

root.mainloop()