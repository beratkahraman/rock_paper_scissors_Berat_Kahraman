import random

def rock_paper_scissors_Berat_Kahraman():
    options = ["rock", "paper", "scissors"]

    print("Welcome to the Rock, Paper, Scissors game!")
    print("Game rules:")
    print("- Rock beats scissors.")
    print("- Paper beats rock.")
    print("- Scissors beat paper.")
    print("- The first to win two rounds wins the game.")
    print("Type 'exit' if you want to quit the game.")
    print("Good Luck :)")


    while True:
        user_score = 0
        computer_score = 0

        while user_score < 2 and computer_score < 2:
            user_choice = input("Choose Rock, Paper, Scissors, or Exit: ").lower()
            if user_choice == "exit":
                print("Exiting the game...")
                return

            if user_choice not in options:
                print("Invalid choice. Please try again.")
                continue

            computer_choice = random.choice(options)
            print(f"Computer's choice: {computer_choice}")

            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                    (user_choice == "paper" and computer_choice == "rock") or \
                    (user_choice == "scissors" and computer_choice == "paper"):
                print("Congratulations, you won this round!")
                user_score += 1
            else:
                print("Unfortunately, you lost this round!")
                computer_score += 1

            print(f"Score - You: {user_score}, Computer: {computer_score}")

        if user_score == 2:
            print("Congratulations! You won the game!")
        else:
            print("Sorry, the computer won the game!")

        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Game over. Thank you for playing!")
            break


rock_paper_scissors_Berat_Kahraman()
