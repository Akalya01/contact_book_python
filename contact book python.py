import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=6, column=0, padx=10, pady=5)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def view_contacts(self):
        contact_list = ""
        for contact in self.contacts:
            contact_list += f"Name: {contact['Name']}, Phone: {contact['Phone']}\n"
        if contact_list:
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("No Contacts", "No contacts available.")

    def search_contact(self):
        search_term = self.search_entry.get()
        search_results = [contact for contact in self.contacts if
                          search_term.lower() in contact['Name'].lower() or search_term in contact['Phone']]
        if search_results:
            search_list = ""
            for contact in search_results:
                search_list += f"Name: {contact['Name']}, Phone: {contact['Phone']}\n"
            messagebox.showinfo("Search Results", search_list)
        else:
            messagebox.showinfo("No Results", "No matching contacts found.")

root = tk.Tk()
app = ContactBookApp(root)
root.mainloop()
