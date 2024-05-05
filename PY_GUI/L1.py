import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("1000x600")
window.title("PRACTICE_V1")


label = tk.Label(window, text="ALLEN BOBO!", font=("Arial", 12)) # Create a label
label.pack(padx=20, pady=20) # Display the label
#textbox = tk.Text(window, height=10, width=50, font=('Arial',12)) # Create a textbox
#textbox.pack(padx=20, pady=20) # Display the textbox

image_path = "C:\\Users\\USER\\Downloads\\ALLEN.jpg"
image_pil = Image.open(image_path)

# Convert the image to Tkinter-compatible format
image_tk = ImageTk.PhotoImage(image_pil)

image_label = tk.Label(window, image=image_tk)
image_label.pack()



gridframe = tk.Frame(window) # Create a frame
gridframe.columnconfigure(0, weight=1) # Configure the column
gridframe.columnconfigure(1, weight=1) # Configure the column
gridframe.columnconfigure(2, weight=1) # Configure the column

btn1 = tk.Button(gridframe, text="YESS", font=('Arial',12)) # Create a button
btn1.grid(row=0, column=0, sticky="ew") # Display the button

btn2 = tk.Button(gridframe, text="YESS", font=('Arial',12)) # Create a button
btn2.grid(row=0, column=1, sticky="ew") # Display the button

btn3 = tk.Button(gridframe, text="YESS", font=('Arial',12)) # Create a button
btn3.grid(row=0, column=2, sticky="ew") # Display the button

btn4 = tk.Button(gridframe, text="YESS", font=('Arial',12)) # Create a button
btn4.grid(row=1, column=0, sticky="ew") # Display the button

btn5 = tk.Button(gridframe, text="YES", font=('Arial',12)) # Create a button
btn5.grid(row=1, column=2, sticky="ew") # Display the button



gridframe.pack(padx=20, pady=20) # Display the frame



#button = tk.Button(window, text="YAMETE ME KUDASAI!", font=("Arial", 12)) # Create a button
#button.pack(padx=10, pady=10) # Display the button
window.mainloop()
