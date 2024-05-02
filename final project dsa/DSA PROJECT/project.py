import tkinter as tk
from tkinter import ttk, StringVar, END, messagebox
import pandas as pd


class Employee:
    def __init__(self, id, name, role, gender, status):
        self.id = int(id)
        self.name = name
        self.role = role
        self.gender = gender
        self.status = status
        self.next = None

class Developers:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def Enqueue(self, data):
        new = Developers(data)
        temp = self.head
        if not temp:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def printlist(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

class EmployeeLinkedList:
    def __init__(self):
        self.head = None

    def insertion(self, employee):
        if not self.head:
            self.head = employee
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = employee

    def delete(self, name):
        temp = self.head
        if temp and temp.name == name:
            self.head = temp.next
            return
        prev = None
        while temp and temp.name != name:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def update(self, new_id, new_role, new_gender, new_status, name):
        temp = self.head
        while temp and temp.name != name:
            temp = temp.next
        if temp:
            temp.id = new_id
            temp.role = new_role
            temp.gender = new_gender
            temp.status = new_status

    def find(self, name):
        temp = self.head
        while temp and temp.name != name:
            temp = temp.next
        return temp
    

class EmployeeManagementApp:
    def __init__(self, root):
        self.employee_list = EmployeeLinkedList()

        root.title("Employee Management System")
        root.geometry("1150x620")
        root.config(bg="#A2B5CD")
        root.resizable(False, False)

        font1 = ("Arial", 20, "bold")
        font2 = ("Arial", 12, "bold")

        id_label = tk.Label(root, font=font1, text="ID", fg="#1E1E1E", bg="#A2B5CD")
        id_label.place(x=20, y=20)

        self.id_entry = tk.Entry(root, font=font1, fg="#000", bg="#fff", bd=2, width=21)
        self.id_entry.place(x=130, y=20)

        name_label = tk.Label(root, font=font1, text="Name", fg="#1E1E1E", bg="#A2B5CD")
        name_label.place(x=20, y=80)

        self.name_entry = tk.Entry(root, font=font1, fg="#000", bg="#fff", bd=2, width=21)
        self.name_entry.place(x=130, y=80)

        role_label = tk.Label(root, font=font1, text="Role", fg="#1E1E1E", bg="#A2B5CD")
        role_label.place(x=20, y=140)

        self.role_entry = tk.Entry(root, font=font1, fg="#000", bg="#fff", bd=2, width=21)
        self.role_entry.place(x=130, y=140)

        gender_label = tk.Label(root, font=font1, text="Gender", fg="#1E1E1E", bg="#A2B5CD")
        gender_label.place(x=20, y=200)

        option = ["Male", "Female"]
        self.variable1 = StringVar()
        self.variable1.set("Female")
        gender_options = ttk.Combobox(root, font=font1, textvariable=self.variable1, values=option, state="readonly", background="#F8F8FF")
        gender_options.place(x=130, y=200)

        status_label = tk.Label(root, font=font1, text="Status", fg="#1E1E1E", bg="#A2B5CD")
        status_label.place(x=20, y=260)

        self.status_entry = tk.Entry(root, font=font1, fg="#000", bg="#fff", bd=2, width=21)
        self.status_entry.place(x=130, y=260)

        # Buttons for various operations
        add_button = tk.Button(root, command=self.insert_employee, font=font1, text="Add Employee", fg="#fff",
                               bg="#CDAA7D", cursor="hand2", width=18)
        add_button.place(x=20, y=320)

        search_button = tk.Button(root, command=self.search_data, font=font1, text="Search Employee", fg="#fff",
                                 bg="#CDAA7D", bd=2, relief=tk.RAISED, cursor="hand2", width=18)
        search_button.place(x=20, y=410)

        update_button = tk.Button(root, command=self.update_employee, font=font1, text="Update Employee", fg="#fff",
                                  bg="#CDAA7D", bd=2, relief=tk.RAISED, cursor="hand2", width=18)
        update_button.place(x=390, y=410)

        delete_button = tk.Button(root, command=self.delete_selected_employee, font=font1, text="Delete Employee", fg="#fff",
                                  bg="#CDAA7D", bd=2, relief=tk.RAISED, cursor="hand2", width=18)
        delete_button.place(x=760, y=410)

        sort_button = tk.Button(root, command=self.Sorting, font=font1, text="Sort by ID", fg="#fff",
                        bg="#CDAA7D", bd=2, relief=tk.RAISED, cursor="hand2", width=18)
        sort_button.place(x=20, y=500)

        display_developers_button = tk.Button(root, command=self.display_developers, font=font1,text="Display Developers", fg="#fff",
                                               bg="#CDAA7D", bd=2, relief=tk.RAISED,cursor="hand2", width=18)
        display_developers_button.place(x=390, y=500)


        # Creating a treeview widget for displaying employee data
        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure("Treeview", font=font2, foreground="#000", background="#F0F8FF", fieldbackground="#F0F8FF")
        style.map("Treeview", background=[("selected", "#A2B5CD")])

        self.tree = ttk.Treeview(root, height=15)
        self.tree["columns"] = ("ID", "Name", "Role", "Gender", "Status")

        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("ID", anchor=tk.CENTER, width=120)
        self.tree.column("Name", anchor=tk.CENTER, width=120)
        self.tree.column("Role", anchor=tk.CENTER, width=120)
        self.tree.column("Gender", anchor=tk.CENTER, width=100)
        self.tree.column("Status", anchor=tk.CENTER, width=120)

        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Role", text="Role")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Status", text="Status")

        self.tree.place(x=500, y=20)

        self.tree.bind("<ButtonRelease>", self.display_data)


        self.read_from_csv() #loading data from csv file


    def display_developers(self):
        developers_name = ["FIZZA SAEED (65341)","YASEEN(65294)","SHAZMA(65450)"]
        queue=Queue()
        for i in range(len(developers_name)):
            queue.Enqueue(developers_name[i])

        developers_window = tk.Toplevel()
        developers_window.title("Developers")

        developers_label = tk.Label(developers_window, text="List of Developers", font=("Arial", 16, "bold"))
        developers_label.pack()

        for developer in developers_name:
            developer_label = tk.Label(developers_window, text=developer)
            developer_label.pack()
        queue.printlist()

    def read_from_csv(self):
        try:
            df = pd.read_csv("Employee_data.csv")
            for index, row in df.iterrows():
                entry = Employee(
                    row['ID'], row['Employee Name'], row['Role'], row['Gender'], row['Status']
                )
                self.employee_list.insertion(entry)
        except FileNotFoundError:
            pass  # Handle the case where the file doesn't exist


    def save_to_csv(self):
        data = {
            'ID': [],
            'Employee Name': [],
            'Role': [],
            'Gender' : [],
            'Status': []
        }

        temp = self.employee_list.head
        while temp:
            data['ID'].append(temp.id)
            data['Employee Name'].append(temp.name)
            data['Role'].append(temp.role)
            data['Gender'].append(temp.gender)
            data['Status'].append(temp.status)
            temp = temp.next

        df = pd.DataFrame(data)
        df.to_csv("Employee_data.csv", index=False)


    def clear_entries(self):
        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.role_entry.delete(0, END)
        self.variable1.set("Female")
        self.status_entry.delete(0, END)


    def insert_employee(self):
        id_str = self.id_entry.get()
        name = self.name_entry.get()
        role = self.role_entry.get()
        gender = self.variable1.get()
        status = self.status_entry.get()

        if not (id_str and name and role and gender and status):
            messagebox.showerror("Error", "Enter all fields.")
        elif self.employee_list.find(name):
            messagebox.showerror("Error", "Name already exists.")
        else:
            try:
                id = int(id_str)
                new_employee = Employee(id, name, role, gender, status)
                self.employee_list.insertion(new_employee)
                self.add_to_treeview()
                self.save_to_csv()
                self.clear_entries()
                messagebox.showinfo("Success", "Data has been inserted")
            except ValueError:
                messagebox.showerror("Error", "ID must be a valid integer.")

    def delete_selected_employee(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Choose an entry to delete.")
        else:
            name_to_delete = self.tree.item(selected_item, "values")[1]
            self.employee_list.delete(name_to_delete)
            self.add_to_treeview()
            self.save_to_csv()
            self.clear_entries()
            messagebox.showinfo("Success", "Data has been deleted.")

    def search_data(self):
        name_to_search = self.name_entry.get()
        if not name_to_search:
            messagebox.showerror("Error", "Enter a name to search for the entry.")
        else:
            matching_entries = self.get_matching_entries(name_to_search)
            self.display_search_results(matching_entries, name_to_search)

    def get_matching_entries(self, name):
        matching_entries = []
        temp = self.employee_list.head
        while temp:
            if temp.name.lower() == name.lower():
                matching_entries.append(temp)
            temp = temp.next
        return matching_entries

    def display_search_results(self, matching_entries, name_to_search):
        search_results_window = tk.Toplevel()
        search_results_window.title("Search Results")

        search_results_label = tk.Label(search_results_window, text=f"Search Results for '{name_to_search}'", font=("Arial", 16, "bold"))
        search_results_label.pack()
        if not matching_entries:
            no_results_label = tk.Label(search_results_window, text="No matching entries found.", font=("Arial", 12))
            no_results_label.pack()
        else:
            for entry in matching_entries:
                entry_label = tk.Label(search_results_window, text=f"{entry.id} - {entry.name} - {entry.role} - {entry.gender} - {entry.status}")
                entry_label.pack()

    def update_employee(self):
        name_to_update = self.name_entry.get()
        if not name_to_update:
            messagebox.showerror("Error", "Enter a name to search for the entry.")
        else:
            selected_item = self.employee_list.find(name_to_update)
            if not selected_item:
                messagebox.showerror("Error", "Choose an employee to update")
            else:
                Id = self.id_entry.get()
                role = self.role_entry.get()
                gender = self.variable1.get()
                status = self.status_entry.get()
                self.employee_list.update(Id, role, gender, status, name_to_update)
                self.add_to_treeview()
                self.save_to_csv()
                self.clear_entries()
                messagebox.showinfo("Success", "Data has been updated")

    def display_data(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item, "values")
            self.id_entry.delete(0, END)
            self.id_entry.insert(0, item_values[0])
            self.name_entry.delete(0, END)
            self.name_entry.insert(0, item_values[1])
            self.role_entry.delete(0, END)
            self.role_entry.insert(0, item_values[2])
            self.variable1.set(item_values[3])
            self.status_entry.delete(0, END)
            self.status_entry.insert(0, item_values[4])

    def add_to_treeview(self):
        self.tree.delete(*self.tree.get_children())
        temp = self.employee_list.head
        while temp:
            self.tree.insert("", END, values=(temp.id, temp.name, temp.role, temp.gender, temp.status))
            temp = temp.next


    def Sorting(self):
        items = []
        temp = self.employee_list.head
        while temp:
            items.append((temp.id, temp.name, temp.role, temp.gender, temp.status))
            temp = temp.next

        def partition(low, high):
            pivot = items[high]
            i = low - 1
            for j in range(low, high):
                if items[j][0] <= pivot[0]:
                    i += 1
                    items[i], items[j] = items[j], items[i]
            items[i + 1], items[high] = items[high], items[i + 1]
            return i + 1

        def quicksort():
            stack = []
            stack.append(0)
            stack.append(len(items) - 1)

            while stack:
                high = stack.pop()
                low = stack.pop()

                pivot_index = partition(low, high)

                if pivot_index - 1 > low:
                    stack.append(low)
                    stack.append(pivot_index - 1)

                if pivot_index + 1 < high:
                    stack.append(pivot_index + 1)
                    stack.append(high)

        quicksort()

        self.tree.delete(*self.tree.get_children())
        for item in items:
            self.tree.insert("", END, values=item)



if __name__ == "__main__":
    app = tk.Tk()
    employee_management_app = EmployeeManagementApp(app)
    app.mainloop()
