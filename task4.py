import tkinter as tk
from tkinter import messagebox

def calculate():
    value = entry.get()
    if value == "":
        messagebox.showerror("Ошибка", "Введите число")
        return
    try:
        number = float(value)
    except:
        messagebox.showerror("Ошибка", "Введите корректное число")
        return
    if number < 0:
        messagebox.showerror("Ошибка", "Число не должно быть отрицательным")
        return
    result = number * 2
    result_label.config(text=f"Результат: {result}", fg="green")

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Результат:", fg="black")

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root)
entry.pack(pady=10)

btn = tk.Button(root, text="Вычислить", command=calculate)
btn.pack(pady=5)

clear_btn = tk.Button(root, text="Очистить", command=clear)
clear_btn.pack(pady=5)

result_label = tk.Label(root, text="Результат:")
result_label.pack(pady=10)

root.mainloop()