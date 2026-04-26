#GUI Game
import random
import tkinter as tk

# main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# choices
choices = ["rock", "paper", "scissors"]

# function
def play(user_choice):
    computer_choice = random.choice(choices)

    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie 😐"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = "You Win 🎉"
    else:
        result = "Computer Wins 🤖"

    label_result.config(
        text=f"You: {user_choice} | Computer: {computer_choice}\n{result}"
    )

# buttons
btn_rock = tk.Button(root, text="🪨 Rock", width=15, command=lambda: play("rock"))
btn_paper = tk.Button(root, text="📄 Paper", width=15, command=lambda: play("paper"))
btn_scissors = tk.Button(root, text="✂️ Scissors", width=15, command=lambda: play("scissors"))

btn_rock.pack(pady=5)
btn_paper.pack(pady=5)
btn_scissors.pack(pady=5)

# result label
label_result = tk.Label(root, text="Make your choice!", font=("Arial", 12))
label_result.pack(pady=10)

# run app
root.mainloop()