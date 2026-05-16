import random

# Games/functions #
num_of_tries = 5
points = 0

#Guess The Number Game
def guess_num():
    global points
    tries = num_of_tries
    random_num = random.randint(1, 20)
    print("Let's Play Guess The Number")
    print(f"You Have {tries} In This Game Mode.\nPoints: {points}")

    while tries > 0:
        try:
            g_num = int(input("Enter A Guess?: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if g_num > random_num:
            tries -= 1
            print("Too High! Try Again")
            print(f"{tries} Tries Left.")
        elif g_num < random_num:
            tries -= 1
            print("Too Low! Try Again")
            print(f"{tries} Tries Left.")
        else:
            points += 100
            print("Congrats! You Guessed Correctly!")
            print(f"You Have {points} Points!")
            return

    print(f"Game over! The number was {random_num}. Points: {points}")

#Rock, Paper, Scissors 
def rock_paper():
    global points
    tries = num_of_tries
    print("Let's Play Rock, Paper, Scissors!")
    choices = ["ROCK", "PAPER", "SCISSORS"]

    while tries > 0:
        user_input = input("Rock, Paper, or Scissors?: ").upper()
        if user_input not in choices:
            print("Please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_input == computer_choice:
            print("It's a tie!")
        elif (
            (user_input == "ROCK" and computer_choice == "SCISSORS")
            or (user_input == "PAPER" and computer_choice == "ROCK")
            or (user_input == "SCISSORS" and computer_choice == "PAPER")
        ):
            points += 100
            print("Congrats! You have won this round!")
        else:
            print("Computer has won this round!")

        tries -= 1
        print(f"Points: {points}")
        print(f"{tries} Tries Left")

    print("Rock, Paper, Scissors game over!")



# Main Menu #
print("Hello! Welcome To Ayanna's Mini Games")
name = input("What Is Your Name?: ")
while True:
    print("1.) Guess The Number \n2.) Rock, Paper, Scissors \n3.) Quit")
    select_game = input(f"Welcome {name}! Choose A Game (1-3): ").strip()

    if select_game == "1":
        guess_num()
    elif select_game == "2":
        rock_paper()
    elif select_game == "3":
        print("Goodbye!")
        break
