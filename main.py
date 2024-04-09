import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

class myGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("List Manager")
        self.geometry("300x500")
        self.resizable(False,True)
        
        self.label = tk.Label(self, text="List Manager", font=("Impact",18), pady=10)
        self.label.pack()
        self.menu()
        self.list()

    #Pinaka main frame
    def list(self):
        self.frame = tk.Frame(self, padx=30, pady=10)        
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.frame, font=("Times", 30))
        self.listbox.pack(fill=tk.BOTH, expand=True)

    #Menubar sa taas
    def menu(self):
        menubar = tk.Menu(self)
        
        #File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        menubar.add_cascade(label="File", menu=file_menu)
        
        #Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Add", command=self.add_item)
        edit_menu.add_command(label="Delete", command=self.delete_item)
        edit_menu.add_command(label="Edit", command=self.edit_item)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        
        #Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.display_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.config(menu=menubar)
    
    #File Menu Handling - open file 
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                data = file.readlines()
            self.listbox.delete(0, tk.END)
            for item in data:
                self.listbox.insert(tk.END, item.strip())

    #File Menu Handling - save file 
    def save_file(self):
        items = self.listbox.get(0, tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w') as file:
                for item in items:
                    file.write(item + '\n')

    #Edit Menu Handling - add  
    def add_item(self):
        item = simpledialog.askstring("Add Item", "Enter item:")
        if item:
            self.listbox.insert(tk.END, item)

    #Edit Menu Handling - delete  
    def delete_item(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            for index in reversed(selected_indices):
                self.listbox.delete(index)

    #Edit Menu Handling - edit  
    def edit_item(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            selected_index = selected_indices[0]  # Get the first index from the tuple
            item = self.listbox.get(selected_index)
            new_item = simpledialog.askstring("Edit Item", f"Edit item '{item}':", initialvalue=item)
            if new_item:
                self.listbox.delete(selected_index)
                self.listbox.insert(selected_index, new_item)

    #Help Menu 
    def display_about(self):
        messagebox.showinfo("About", "List Manager\nAuthor: owenlim225")


            
app = myGui()
app.mainloop()
