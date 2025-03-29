from tkinter import *
import tkinter as tk
from listar_procesos import listar_procesos
import psutil
 
colums_added = 1

class Table:
     
    def __init__(self,root):
        root.title("Lista de procesos")
        root.config(background="black")
        root.resizable(True, True)
        root.configure(bg="black")
        
        # create scrollbar
        # Create a canvas to hold the table
        self.canvas = Canvas(root, bg="black")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a frame inside the canvas for the table
        self.table_frame = Frame(self.canvas, bg="black")  # Use this frame for grid
        self.canvas.create_window((0, 0), window=self.table_frame, anchor="nw")

        # Configure the scrollbar to work with the canvas
        self.scrollbar = Scrollbar(root, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Bind the canvas to update the scroll region
        self.table_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(self.table_frame, width=20, fg='white')  # Use table_frame instead of root
                self.e.grid(row=i, column=j)
                if (j < total_columns - 1):
                    self.e.insert(END, lst[i][j])
                    self.e.config(state='readonly')  # Asegurar que permanezca en solo lectura    
                
                if j == total_columns - 1:
                    self.e.config(state='normal')
                    self.e.insert(END, "Kill")
                    self.e.bind("<Button-1>", self.kill_process)
                    
    def kill_process(self, event):
        # Get the process id
        row = event.widget.grid_info()["row"]
        process_id = lst[row][0]
        print(f"Process ID: {process_id}")
        processKill = psutil.Process(int(process_id))
        processKill.terminate()
        

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