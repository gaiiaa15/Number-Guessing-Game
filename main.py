import random
print("*************************WELCOME TO THE NUMBER GUESSING GAME*************************")
print("*************************I'm thinking of a number between 1 and 100*************************\n")
# assigned a random integer between 1 and 100 inclusive for the user to guess
computer_number = random.randint(1, 100)
print(computer_number)


game_difficulty = {
    "easy": 10,
    "medium": 5,
    "hard": 3,
}

print("Please select the difficulty Level:")
# enumerate adds numbers to each level. For example 1. Easy 10 chances
for option_number, difficulty_name in enumerate(game_difficulty, start = 1):
    print(option_number,".", difficulty_name.title(), game_difficulty[difficulty_name], "Chances.")
valid_input = True
while valid_input:
    # asks the user for their level choice
    level_choice = input("\nEnter your choice: ")
    if level_choice == "1":
        allowed_attempts = game_difficulty["easy"]
        valid_input = False
        print(f"Great! You have selected the Easy level.")
        print("Lets get started!")
    elif level_choice == "2":
        allowed_attempts = game_difficulty["medium"]
        valid_input = False
        print(f"Great! You have selected the Medium level.")
        print("Lets get started!")
    elif level_choice == "3":
        allowed_attempts = game_difficulty["hard"]
        valid_input = False
        print(f"Great! You have selected the Hard level.")
        print("Lets get started!")
    else:
        print("Please enter a valid choice")


def play_rounds (user_guess,computer_number, attempts_remaining):
    """counts the number of chances left and determines whether the user won or lost"""
    game_running = True
    attempts_used = 0
    while game_running:
        if not user_guess == computer_number and not attempts_remaining == 0:
            attempts_remaining -= 1
            attempts_used += 1
            if user_guess > computer_number:
                print(f"The number is less than {user_guess}.")
            elif user_guess < computer_number:
                print(f"The number is greater than {user_guess}.")
            print(f"You have {attempts_remaining} chances left.")
            if attempts_remaining == 0:
                print("GAME OVER :(")
                game_running = False
            else:
                user_guess = int(input("\nEnter your guess: "))

        elif  attempts_remaining == 0 and user_guess == computer_number:
                print("WINNER WINNER CHICKEN DINNER!")
                print(f"Took {attempts_used} chances to win.")
                game_running = False
        elif attempts_remaining == 0 and user_guess != computer_number:
                print("GAME OVER :(")
                game_running = False
        elif user_guess == computer_number and not attempts_remaining == 0:
            print("WINNER WINNER CHICKEN DINNER!")
            print(f"Took {attempts_used} chances to win.")
            game_running = False
        else:
            print("Invalid Input")




user_number_guess = int(input("Enter your guess: "))
play_rounds(user_number_guess, computer_number, allowed_attempts)







