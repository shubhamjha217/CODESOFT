import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        self.root.geometry('400x400')
        self.root.config(bg="lightblue")
        tk.Label(text="ROCK-PAPER-SCISSORS",bg="red",width='250',height='2',font=("Calibri",24)).pack()

        self.user_score = 0
        self.computer_score = 0

        self.user_choice = None
        self.computer_choice = None

        self.choices = ["Rock", "Paper", "Scissors"]

        self.user_label = tk.Label(root, text="Your Choice: ",bg="yellow",height="1",width="150")
        self.user_label.pack()
       

        self.user_buttons = []
        for choice in self.choices:
            button = tk.Button(root, text=choice, command=lambda c=choice: self.user_select(c))
            button.pack()
            self.user_buttons.append(button)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.score_label = tk.Label(root, text="Score: You {} - {} Computer".format(self.user_score, self.computer_score))
        self.score_label.pack()

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.pack()
        self.play_again_button.config(state=tk.DISABLED)

    def user_select(self, choice):
        self.user_choice = choice
        self.computer_choice = random.choice(self.choices)
        self.result_label.config(text="Computer chose: {}".format(self.computer_choice))
        self.determine_winner()

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            result = "It's a tie!"
        elif (self.user_choice == "Rock" and self.computer_choice == "Scissors") or \
             (self.user_choice == "Paper" and self.computer_choice == "Rock") or \
             (self.user_choice == "Scissors" and self.computer_choice == "Paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        self.update_scoreboard(result)

    def update_scoreboard(self, result):
        self.score_label.config(text="Score: You {} - {} Computer".format(self.user_score, self.computer_score))
        self.result_label.config(text=result)
        self.play_again_button.config(state=tk.NORMAL)

        for button in self.user_buttons:
            button.config(state=tk.DISABLED)

    def play_again(self):
        self.user_choice = None
        self.computer_choice = None
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)

        for button in self.user_buttons:
            button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
