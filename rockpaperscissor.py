import random
import tkinter as tk
from tkinter import messagebox

def play_game(choice):
    choices = ['Rock', 'Paper', 'Scissors']
    comp_choice = random.choice(choices)

    # Determine the winner
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 'Rock' and comp_choice == 'Scissors') or \
         (choice == 'Paper' and comp_choice == 'Rock') or \
         (choice == 'Scissors' and comp_choice == 'Paper'):
        result = "User wins"
    else:
        result = "Computer wins"

    return comp_choice, result

def main():
    root = tk.Tk()
    root.title("Rock Paper Scissors Game")

    # Create labels and buttons
    label = tk.Label(root, text="Choose your move:")
    label.pack()

    def handle_click(choice):
        comp_choice, result = play_game(choice)
        messagebox.showinfo("Result", f"Your choice: {choice}\nComputer's choice: {comp_choice}\nResult: {result}")

    # Rock button
    rock_button = tk.Button(root, text="Rock", command=lambda: handle_click('Rock'))
    rock_button.pack()

    # Paper button
    paper_button = tk.Button(root, text="Paper", command=lambda: handle_click('Paper'))
    paper_button.pack()

    # Scissors button
    scissors_button = tk.Button(root, text="Scissors", command=lambda: handle_click('Scissors'))
    scissors_button.pack()

    root.mainloop()

# Command-line interface (for reference)
def command_line_game():
    print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
          + "Rock vs Paper -> Paper wins \n"
          + "Rock vs Scissors -> Rock wins \n"
          + "Paper vs Scissors -> Scissor wins \n")

    while True:
        print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

        choice = int(input("Enter your choice :"))

        while choice > 3 or choice < 1:
            choice = int(input('Enter a valid choice please ☺'))

        if choice == 1:
            choice_name = 'Rock'
        elif choice == 2:
            choice_name = 'Paper'
        else:
            choice_name = 'Scissors'

        print('User choice is \n', choice_name)
        print('Now its Computers Turn....')

        comp_choice = random.randint(1, 3)
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)

        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissors'

        print("Computer choice is \n", comp_choice_name)
        print(choice_name, 'Vs', comp_choice_name)

        if choice == comp_choice:
            print('Its a Draw')
            result = "DRAW"

        if (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
            print('Paper wins =>')
            result = 'Paper'

        if (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
            print('Rock wins =>')
            result = 'Rock'

        if (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
            print('Scissors wins =>')
            result = 'Scissors'

        if result == 'DRAW':
            print("<== Its a tie ==>")
        elif result == choice_name:
            print("<== User wins ==>")
        else:
            print("<== Computer wins ==>")

        print("Do you want to play again? (Y/N)")
        ans = input().lower()
        if ans == 'n':
            break

    print("thanks for playing")

if __name__ == "__main__":
    # Start the GUI game
    main()
