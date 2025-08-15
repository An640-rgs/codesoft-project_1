import random
import tkinter as tk
from tkinter import messagebox

# Determine game result
def gameWin(comp, you):
    if comp == you:
        return "Tie"
    elif (comp == 'r' and you == 's') or (comp == 's' and you == 'p') or (comp == 'p' and you == 'r'):
        return "Lose"
    else:
        return "Win"

# Function to handle user's choice
def play(user_choice):
    choices = ['r', 'p', 's']
    comp_choice = random.choice(choices)

    # Mapping for display
    choice_map = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

    result = gameWin(comp_choice, user_choice)

    result_text = (
        f"Computer chose: {choice_map[comp_choice]}\n"
        f"You chose: {choice_map[user_choice]}\n\n"
        f"Result: You {result}!"
    )

    result_label.config(text=result_text)

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)

# Heading
tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 18, "bold")).pack(pady=10)

# Buttons for choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play('r'))
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play('p'))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play('s'))

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14), justify="center")
result_label.pack(pady=20)

# Run the GUI
root.mainloop()
