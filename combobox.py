#Import the tkinter as tk
import tkinter as tk
from tkinter import ttk


#Creating the event (on Select)
def on_select(event):
    
    selected_item = event.widget.get()
    print("Selected item:", selected_item)
    
#Create root window for the widget
root = tk.Tk()
root.title("Combobox Example")
    
#Creating static array 
items = ["Item 1", "Item 2","Item 3","Item 4","Item 5"]

#Tie the static array with the combobox created
combo_box = ttk.Combobox(root, values=items)

#Bind the function with selected item to the on select function
combo_box.bind("<<ComboboxSelected>>", on_select)

#Makes the widget fill in the entire frame
combo_box.pack()

#Loops forever until user ends it
root.mainloop()
