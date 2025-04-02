import tkinter as tk

#create a window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x300")
root.resizable(False, False)

#variable to hold inputs
input = tk.StringVar()

#calculator display
display = tk.Entry(root, textvariable=input, font=("Arial", 20), justify="right", relief=tk.SUNKEN)
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10, sticky="nsew")

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

buttons = [("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), 
           ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), 
           ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), 
           ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3)]

def calculate():
    """evaluate the expression in the display"""
    try:
        result = eval(input.get())
        input.set(result)
    except ZeroDivisionError:
        input.set("Division by zero")
    except Exception as e:
        input.set(f"Error: {e}")

def buttonClick(value):
    """add clicked button value to display"""
    current = input.get()
    input.set(current + str(value))

def clear():
    """clear the display"""
    input.set("")

#creating and placing buttons
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2, command=calculate)
    else:
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2, command=lambda t=text: buttonClick(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

clear_button = tk.Button(root, text="C", font=("Arial", 20), width=21, height=2, command=clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

#run the main loop
root.mainloop()