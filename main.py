from tkinter import *
from listar_procesos import listar_procesos
 
colums_added = 1

class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='white') 
                self.e.grid(row=i, column=j)
                if (j < total_rows):
                    self.e.insert(END, lst[i][j])
                    self.e.config(state='readonly')  # Asegurar que permanezca en solo lectura    
                
                if j == total_columns - 1:
                    self.e.config(state='normal')
                    self.e.insert(END, "Kill")
                    self.e.bind("<Button-1>", self.kill_process)
                    
    def kill_process(self, event):
        # Get the process id
        process_id = event.widget.get()
        # Kill the process
        print("Killing process with id: ", process_id)

process = listar_procesos()

# take the data
lst = tuple(process[:5])

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])+colums_added
  
# create root window
root = Tk()
t = Table(root)
root.mainloop()