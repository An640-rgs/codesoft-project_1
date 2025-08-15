import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry to show the expression
expression = ""
input_text = tk.StringVar()

input_frame = tk.Frame(root, width=300, height=50, bd=0, highlightbackground="black", highlightthickness=1)
input_frame.pack(side="top")

input_field = tk.Entry(input_frame, font=('arial', 18), textvariable=input_text, width=50, bg="#eee", bd=0, justify="right")
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # inner padding

# Function to update expression
def press(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))  # risky in general, but fine for calculator
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Function to clear the entry field
def clear():
    global expression
    expression = ""
    input_text.set("")

# Buttons layout
btns_frame = tk.Frame(root, bg="grey")
btns_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn = tk.Button(
            btns_frame, text=btn_text, fg="black", width=10, height=3,
            bd=0, bg="#fff", cursor="hand2",
            command=lambda txt=btn_text: (
                clear() if txt == "C" else equalpress() if txt == "=" else press(txt)
            )
        )
        btn.grid(row=i, column=j, padx=1, pady=1)

# Start GUI loop
root.mainloop()