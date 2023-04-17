import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from ttkthemes import ThemedStyle
from tkinter import ttk
from domains.information import Information
from domains.Death_Declaration import DeathDeclaration
from domains.Marriage import Marriage
from domains.Birth_declaration import BirthDeclaration

# Create a new Tkinter window
root = tk.Tk()

# Set the window size and title
root.geometry("430x490+500+130")
root.title("PGSIM")


# Create a themed style object
style = ThemedStyle(root)
style.set_theme("equilux")

# Create a PhotoImage object--
image = PhotoImage(file="Interface\khanh.png")
# Create a Label widget with the image
label = Label(root, image=image)

# Plack the Label widget
label.place(x=-37, y=50)

canvas3 = tk.Canvas(root, width=500, height=50, bg="#0C090A", highlightthickness=0)
canvas3.place(x = 0, y = 20)

# Set the window background color
root.configure(bg='#0C090A')

canvas = tk.Canvas(root, width=30, height=500, bg="#003366", highlightthickness=0)
canvas.place(x = 0, y = 0)

canvas2 = tk.Canvas(root, width=30, height=500, bg="#003366", highlightthickness=0)
canvas2.place(x = 400, y = 0)


def add_info():
    add_window = tk.Toplevel(root)
    app = Information(add_window)

def update_info():
    update_window = tk.Toplevel(root)
    app = Marriage(update_window)

def delete_info():
    delete_window = tk.Toplevel(root)
    app = BirthDeclaration(delete_window)

def search_info():
    search_window = tk.Toplevel(root)
    app = DeathDeclaration(search_window)

style = ttk.Style()

# define a custom color for the button
style.map("TButton", background=[("active", "#00008B"), ("!disabled", "#8D918D")])
style.configure("TButton",relief='groove', bordercolor="#8D918D", borderwidth=2)

# Create the buttons with a fixed size
button_width = 40
button_height = 4
add_button = ttk.Button(root, text="Citizens information", command=add_info, width=button_width, padding=button_height)
update_button = ttk.Button(root, text="Marriage declaration", command=update_info, width=button_width, padding=button_height)
delete_button = ttk.Button(root, text="Birth certificate", command=delete_info, width=button_width, padding=button_height)
search_button = ttk.Button(root, text="Death declaratiom", command=search_info, width=button_width, padding=button_height)

# Add the buttons to the window
add_button.place(x=215, y=150+64, anchor = "center")
update_button.place(x=215, y=200+64, anchor = "center")
delete_button.place(x=215, y=250+64, anchor = "center")
search_button.place(x=215, y=300+64, anchor = "center")


frame = tk.Frame(root, width=328, height=72, bg="black", relief="solid", highlightbackground="#003366", highlightthickness=5)
frame.place(x=49, y=30)

text_label = tk.Label(root, text="GOVERNMENTAL INFORMATION MANAGEMENT SYSTEM", fg="#00008B", bg="#8D918D",font=("Segoe UI",15,"bold"),wraplength=400, anchor="center")
text_label.place(x=54, y=35)

root.mainloop()



'''
# Create a frame with a gray background and blue border
board_frame = tk.Frame(root, width=10, height=500, bg="gray", relief="solid", highlightbackground="#003366", highlightthickness=5)
board_frame.place(x=345, y=73)

# Add a label to display stored information 
info_label = tk.Label(board_frame, text="Display", font=("Calibri", 16))
info_label.place(x=10, y=10)
'''
