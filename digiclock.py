from tkinter import *
from time import strftime

# Create the main window
root = Tk()
root.title("Digital Clock")
root.geometry("350x150")
root.configure(bg="black")

# Function to update the time
def time():
    string = strftime('%H:%M:%S %p')  # Format: Hour:Minute:Second AM/PM
    label.config(text=string)
    label.after(1000, time)  # Update every 1000 milliseconds (1 second)

# Styling the clock label
label = Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

# Start the clock
time()
root.mainloop()
