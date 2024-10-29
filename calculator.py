import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Rich Python Calculator")

        self.expression = ""
        self.memory = 0

        self.input_field = tk.Entry(root, width=40, borderwidth=5)
        self.input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'M+', 'M-', 'MR',
            '√', '^', 'sin', 'cos'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.root, text=button, padx=20, pady=20, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression.replace('^', '**')))
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, self.expression)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
                self.clear_input()
        elif char == 'C':
            self.clear_input()
        elif char == 'M+':
            self.memory += float(self.input_field.get() or 0)
            self.clear_input()
        elif char == 'M-':
            self.memory -= float(self.input_field.get() or 0)
            self.clear_input()
        elif char == 'MR':
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, self.memory)
        elif char in ['√', 'sin', 'cos']:
            try:
                value = float(self.input_field.get())
                if char == '√':
                    result = math.sqrt(value)
                elif char == 'sin':
                    result = math.sin(math.radians(value))
                elif char == 'cos':
                    result = math.cos(math.radians(value))
                self.clear_input()
                self.input_field.insert(0, result)
            except ValueError:
                messagebox.showerror("Error", "Invalid input for trigonometric/square root operation.")
                self.clear_input()
        else:
            self.expression += str(char)
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, self.expression)

    def clear_input(self):
        self.expression = ""
        self.input_field.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
