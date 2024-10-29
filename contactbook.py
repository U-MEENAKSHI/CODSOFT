import tkinter as tk
from tkinter import messagebox
import json
import os

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = {}
        self.load_contacts()

        # UI Components
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.pack(pady=5)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.display_button = tk.Button(root, text="Display Contacts", command=self.display_contacts)
        self.display_button.pack(pady=5)

        self.contacts_listbox = tk.Listbox(root, width=50, height=10)
        self.contacts_listbox.pack(pady=10)

        self.save_button = tk.Button(root, text="Save Contacts", command=self.save_contacts)
        self.save_button.pack(pady=5)

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if name and phone:
            self.contacts[name] = phone
            self.update_contacts_listbox()
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Both name and phone number must be filled.")

    def delete_contact(self):
        try:
            selected_contact = self.contacts_listbox.get(self.contacts_listbox.curselection())
            name = selected_contact.split(" - ")[0]
            del self.contacts[name]
            self.update_contacts_listbox()
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def search_contact(self):
        name = self.name_entry.get().strip()
        if name in self.contacts:
            phone = self.contacts[name]
            messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {phone}")
        else:
            messagebox.showwarning("Warning", "Contact not found.")

    def display_contacts(self):
        self.update_contacts_listbox()

    def update_contacts_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for name, phone in self.contacts.items():
            self.contacts_listbox.insert(tk.END, f"{name} - {phone}")

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file)
        messagebox.showinfo("Info", "Contacts saved successfully!")

    def load_contacts(self):
        if os.path.exists("contacts.json"):
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
            self.update_contacts_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()
