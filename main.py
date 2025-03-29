from tkinter import *
import tkinter as tk
from listar_procesos import listar_procesos
import psutil
 
colums_added = 3

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
        
        # Create a horizontal scrollbar
        self.h_scrollbar = Scrollbar(root, orient=HORIZONTAL, command=self.canvas.xview)
        self.h_scrollbar.pack(side=BOTTOM, fill=X)
        self.canvas.config(xscrollcommand=self.h_scrollbar.set)

        # Bind the canvas to update the scroll region
        self.table_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        # Configure static column widths
        
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(self.table_frame, width=20, fg='white')  # Width in characters
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