import tkinter as tk
from tkinter import messagebox

def validate_input(value):
    if value == "":
        messagebox.showerror("Ошибка", "Введите число")
        return None
    try:
        number = float(value)
    except:
        messagebox.showerror("Ошибка", "Введите корректное число")
        return None
    if number < 0:
        messagebox.showerror("Ошибка", "Число не должно быть отрицательным")
        return None
    return number

def calculate_square(number):
    return number * number

def on_button_click():
    value = entry.get()
    number = validate_input(value)
    if number is None:
        return
    result = calculate_square(number)
    result_label.config(text=f"Результат: {result}", fg="green")

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="Результат:", fg="black")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root)
entry.pack(pady=10)

btn = tk.Button(root, text="Вычислить", command=on_button_click)
btn.pack(pady=5)

clear_btn = tk.Button(root, text="Очистить", command=clear)
clear_btn.pack(pady=5)

result_label = tk.Label(root, text="Результат:")
result_label.pack(pady=10)

root.mainloop()