import tkinter as tk
from tkinter import ttk

def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def add_to_display(char):
    entry.insert(tk.END, char)

root = tk.Tk()
root.title("Advanced Calculator")

entry = ttk.Entry(root, width=40, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]


for (text, row, column) in buttons:
    ttk.Button(root, text=text, width=10, command=lambda t=text: add_to_display(t)).grid(row=row, column=column, padx=5, pady=5)

ttk.Button(root, text="Clear", width=10, command=clear).grid(row=5, column=0, columnspan=2, padx=5, pady=5)

ttk.Button(root, text="Eval", width=10, command=evaluate_expression).grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()