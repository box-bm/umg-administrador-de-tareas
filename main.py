from tkinter import *
import tkinter as tk
from listar_procesos import listar_procesos
import psutil
 
colums_added = 3

class Table:
     
    def __init__(self,root):
        root.title("Lista de procesos")
        root.config(background="white")
        root.resizable(True, True)
        root.configure(bg="white")
        root.geometry("900x600")
        
        # Add input field for filtering by name
        self.filter_frame = Frame(root, bg="white")
        self.filter_frame.pack(fill=X)
        
        Label(self.filter_frame, text="Filtrar:", bg="white", fg="black").pack(side=LEFT, padx=5)
        self.filter_entry = Entry(self.filter_frame, width=30)
        self.filter_entry.pack(side=LEFT, padx=5)
        self.filter_entry.bind("<Return>", self.filter_processes)
        
        Button(self.filter_frame, text="find", command=self.filter_processes, bg="blue", fg="white", activeforeground="white", activebackground="black").pack(side=LEFT, padx=5)
        Button(self.filter_frame, text="Clear", command=self.clear_filter, bg="red", fg="white", activeforeground="white", activebackground="black").pack(side=LEFT, padx=5)
        
        # create scrollbar
        # Create a canvas to hold the table
        self.canvas = Canvas(root, bg="white")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a frame inside the canvas for the table
        self.table_frame = Frame(self.canvas, bg="white")  # Use this frame for grid
        self.canvas.create_window((0, 0), window=self.table_frame, anchor="nw")

        # Configure the scrollbar to work with the canvas
        self.scrollbar = Scrollbar(root, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Bind the canvas to update the scroll region
        self.table_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        # Configure static column widths
        
        # code for creating table
        self.create_table()
                    
    def kill_process(self, event):
        row = event.widget.grid_info()["row"]
        process_id = lst[row][0]
        processKill = psutil.Process(int(process_id))
        processKill.terminate()
        
    def suspend_process(self, event):
        row = event.widget.grid_info()["row"]
        process_id = lst[row][0]
        processKill = psutil.Process(int(process_id))
        processKill.suspend()
        
    def resume_process(self, event):
        row = event.widget.grid_info()["row"]
        process_id = lst[row][0]
        processKill = psutil.Process(int(process_id))
        processKill.resume()

    def filter_processes(self, event=None):  # Make 'event' optional
        filter_text = self.filter_entry.get().lower()
        filtered_data = [row for row in process if filter_text in row[1].lower()]
        
        global lst, total_rows
        lst = tuple(filtered_data[:100])
        total_rows = len(lst)
        
        # Clear and refresh the table
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        self.create_table()

    def clear_filter(self):
        self.filter_entry.delete(0, END)
        self.filter_processes(None)

    def create_table(self):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(self.table_frame, width=20, fg='black')  # Width in characters
                self.e.grid(row=i, column=j)
                if (j < total_columns - colums_added):
                    self.e.insert(END, lst[i][j])
                    columnWidth = 10
                    if j == 1: # Nombre
                        columnWidth = 30
                    self.e.config(state='readonly', width=columnWidth)  # Asegurar que permanezca en solo lectura    
                
                if j == total_columns - 3:
                    self.e.config(state='normal', bg='orange', width=10)
                    self.e.insert(END, "Suspend")
                    self.e.bind("<Button-1>", self.suspend_process)
                    
                if j == total_columns - 2:
                    self.e.config(state='normal', bg='green', width=10)
                    self.e.insert(END, "resume")
                    self.e.bind("<Button-1>", self.resume_process)
                    
                if j == total_columns - 1:
                    self.e.config(state='normal', bg='red', width=10)
                    self.e.insert(END, "Kill")
                    self.e.bind("<Button-1>", self.kill_process)
 
process = listar_procesos()

# take the data
lst = tuple(process[:100])

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])+colums_added
  
# create root window
root = Tk()
t = Table(root)
root.mainloop()