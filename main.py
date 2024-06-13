import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    return user_choice

def get_computer_choice(difficulty, user_choice):
    if difficulty == "easy":
        return random.choices(["rock", "paper", "scissors"],
                              weights=[1, 1, 2] if user_choice == "rock" else
                                      [2, 1, 1] if user_choice == "paper" else
                                      [1, 2, 1])[0]
    elif difficulty == "normal":
        return random.choice(["rock", "paper", "scissors"])
    elif difficulty == "hard":
        return random.choices(["rock", "paper", "scissors"],
                              weights=[2, 1, 1] if user_choice == "rock" else
                                      [1, 2, 1] if user_choice == "paper" else
                                      [1, 1, 2])[0]
    elif difficulty == "ace":
        return {"rock": "paper", "paper": "scissors", "scissors": "rock"}[user_choice]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def get_difficulty():
    difficulty = input("Choose difficulty (easy - $50, normal - $100, hard - $500, ace - $1000): ").strip().lower()
    while difficulty not in ["easy", "normal", "hard", "ace"]:
        print("Invalid choice. Please try again.")
        difficulty = input("Choose difficulty (easy, normal, hard, ace): ").strip().lower()
    return difficulty

def play_game():
    money = 100
    print("Welcome to Rock, Paper, Scissors Money Match!")
    print(f"You start with ${money}.")

    while money > 0:
        difficulty = get_difficulty()
        cost = {"easy": 50, "normal": 100, "hard": 500, "ace": 1000}[difficulty]

        if money < cost:
            print(f"Insufficient funds to play on {difficulty} difficulty. You have ${money}.")
            continue

        user_choice = get_user_choice()
        computer_choice = get_computer_choice(difficulty, user_choice)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            earnings = cost * 2
            money += earnings
            print(f"You won ${earnings}! Your total money is now ${money}.")

        elif result == "It's a tie!":
            print(f"It's a tie! Your total money remains ${money}.")

        else:
            money -= cost
            print(f"You lost ${cost}. Your total money is now ${money}.")

        if money <= 0:
            print("You have run out of money. Game over.")
            break

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print(f"You finished with ${money}. Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
