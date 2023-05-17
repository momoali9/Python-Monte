#Importing class tkinter and renaming it tk
import tkinter as tk


#Creating function for button click
def button_click():
    print("Button clicked!")


#Create the root window
root = tk.Tk()
root.title("Button Example")

#Create Button object which will have 3 arguments
button = tk.Button(root,text="Click Me!", command=button_click)
button.pack()

#mainloop
root.mainloop()