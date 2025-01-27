import random
import tkinter as tk
import pygame

# Initialize Pygame for sounds
pygame.mixer.init()

# Load sound effects
win_sound = pygame.mixer.Sound("sounds/win.wav")
lose_sound = pygame.mixer.Sound("sounds/lose.wav")
tie_sound = pygame.mixer.Sound("sounds/tie.wav")


# Possible choices
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "win"
    else:
        return "lose"

# Function to handle user choice
def play_round(user_choice):
    global user_score, computer_score

    # Computer's choice
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)

    # Update the GUI based on the result
    if result == "win":
        result_label.config(text=f"You win! Computer chose {computer_choice}.", fg="green")
        user_score += 1
        pygame.mixer.Sound.play(win_sound)
    elif result == "lose":
        result_label.config(text=f"You lose! Computer chose {computer_choice}.", fg="red")
        computer_score += 1
        pygame.mixer.Sound.play(lose_sound)
    else:
        result_label.config(text=f"It's a tie! Both chose {computer_choice}.", fg="blue")
        pygame.mixer.Sound.play(tie_sound)

    # Update scores
    score_label.config(text=f"Score: You {user_score} - {computer_score} Computer")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your choice to start the game!")
    score_label.config(text="Score: You 0 - 0 Computer")

# Initialize scores
user_score = 0
computer_score = 0

# Create the main Tkinter window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Add widgets
result_label = tk.Label(root, text="Make your choice to start the game!", font=("Arial", 14))
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 12))
score_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Buttons for choices
rock_button = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 12), command=lambda: play_round("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="📄 Paper", font=("Arial", 12), command=lambda: play_round("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="✂️ Scissors", font=("Arial", 12), command=lambda: play_round("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Reset button
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_game)
reset_button.pack(pady=10)

# Run the main event loop
root.mainloop()