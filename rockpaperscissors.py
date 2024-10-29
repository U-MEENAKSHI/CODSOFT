import tkinter as tk
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.score_label = tk.Label(root, text="Score: You - 0 | Computer - 0", font=("Helvetica", 14))
        self.score_label.pack(pady=20)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=20)

        self.rock_button = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.play("Rock"))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.play("Paper"))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.play("Scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.reset_button = tk.Button(root, text="Reset Scores", command=self.reset_scores)
        self.reset_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = ""

        if user_choice == computer_choice:
            result = f"It's a tie! Both chose {user_choice}."
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = f"You win! {user_choice} beats {computer_choice}."
            self.user_score += 1
        else:
            result = f"You lose! {computer_choice} beats {user_choice}."
            self.computer_score += 1

        self.update_score(result, computer_choice)

    def update_score(self, result, computer_choice):
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score: You - {self.user_score} | Computer - {self.computer_score}")

    def reset_scores(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score: You - 0 | Computer - 0")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    rps_game = RPSGame(root)
    root.mainloop()
