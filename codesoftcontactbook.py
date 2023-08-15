import tkinter as tk
from tkinter import messagebox

class ContactBook:
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
        self.add_button.grid(row=4, column=0, padx=10, pady=5)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=4, column=1, padx=10, pady=5)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=4, column=2, padx=10, pady=5)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=3, padx=10, pady=5)

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=5, column=0, padx=10, pady=5)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=5, column=1, padx=10, pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=5, column=2, padx=10, pady=5)

        self.contact_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.contact_listbox.grid(row=6, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

        self.contact_listbox.bind("<<ListboxSelect>>", self.on_contact_select)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            self.contact_listbox.insert(tk.END, name)
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if name and phone and email and address:
                selected_contact["Name"] = name
                selected_contact["Phone"] = phone
                selected_contact["Email"] = email
                selected_contact["Address"] = address
                self.contact_listbox.delete(selected_index[0])
                self.contact_listbox.insert(selected_index[0], name)
                self.clear_entries()
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showerror("Error", "Please fill in all the fields.")
        else:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            del self.contacts[selected_index[0]]
            self.contact_listbox.delete(selected_index[0])
            self.clear_entries()
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Please select a contact to delete.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("No Contacts", "Contact book is empty.")
        else:
            contact_list = ""
            for contact in self.contacts:
                contact_list += f"Name: {contact['Name']}\nPhone: {contact['Phone']}\nEmail: {contact['Email']}\nAddress: {contact['Address']}\n\n"
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        search_value = self.search_entry.get()
        if search_value:
            found_contacts = []
            for contact in self.contacts:
                if search_value.lower() in contact["Name"].lower() or search_value in contact["Phone"]:
                    found_contacts.append(contact)

            if found_contacts:
                self.contact_listbox.delete(0, tk.END)
                for contact in found_contacts:
                    self.contact_listbox.insert(tk.END, contact["Name"])
            else:
                messagebox.showinfo("No Results", "No contacts found for the given search value.")
        else:
            self.populate_listbox()

    def on_contact_select(self, event):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, selected_contact["Name"])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, selected_contact["Phone"])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, selected_contact["Email"])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(tk.END, selected_contact["Address"])

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def populate_listbox(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, contact["Name"])

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
