import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.include_uppercase = tk.BooleanVar()
        self.uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.include_uppercase)
        self.uppercase_check.pack()

        self.include_numbers = tk.BooleanVar()
        self.numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=self.include_numbers)
        self.numbers_check.pack()

        self.include_special = tk.BooleanVar()
        self.special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special)
        self.special_check.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, width=40)
        self.password_entry.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Password length must be greater than zero.")

            characters = string.ascii_lowercase  # Start with lowercase letters

            if self.include_uppercase.get():
                characters += string.ascii_uppercase
            if self.include_numbers.get():
                characters += string.digits
            if self.include_special.get():
                characters += string.punctuation

            if not characters:
                raise ValueError("At least one character type must be selected.")

            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
