"""
All Imports
"""
import random
import time

# List of categories for guessing word
countries = ["switzerland", "germany", "canada",
             "sweden", "japan", "australia"]
sports = ["soccer", "badminton", "hockey", "volleyball",
          "basketball", "tennis", "golf"]
animals = ["elephant", "lion", "leopard",
           "buffalo", "rhino", "monkey", "tiger"]
drinks = ["tequila", "vermouth", "cognac",
          "whiskey", "water", "baileys"]

category = [countries, sports, animals, drinks]

# stages for wrong answer  https://enhancer298.net/2020/07/10/hangman1
stages = ['___________________',
          '|         |        ',
          '|         |        ',
          '|         |        ',
          '|         0        ',
          '|        /|＼      ',
          '|        / ＼      ',
          '|      THE END     ']

# Setting the stage number to be used as a limit for incorrect attempts
stage_num = len(stages)


def display_title():
    """
    Prompt user to input name and greetings
    """
    # Title ASCII ART https://patorjk.com/software/taag
    print(" __      _____ _    ___ ___  __  __ ___   _____ ___ ")
    print(" \ \    / / __| |  / __/ _ \|  \/  | __| |_   _/ _ \ ")
    print("  \ \/\/ /| _|| |_| (_| (_) | |\/| | _|    | || (_) |")
    print("   \_/\_/ |___|____\___\___/|_|  |_|___|   |_| \___/  \n")     
    print(" _  _   _   _  _  ___ __  __   _   _  _    ___   _   __  __ ___ ")
    print("| || | /_\ | \| |/ __|  \/  | /_\ | \| |  / __| /_\ |  \/  | __|")
    print("| __ |/ _ \| .` | (_ | |\/| |/ _ \| .` | | (_ |/ _ \| |\/| | _| ")
    print("|_||_/_/ \_\_|\_|\___|_|  |_/_/ \_\_|\_|  \___/_/ \_\_|  |_|___|\n")


def welcome():
    """
    Ask user to input name and print greetings
    """
    name = input("Enter your name: ")
    if name:
        print(f"\nHello {name.upper()}\n")
    else:
        print("\nHello Guest, Best of luck!\n")
    time.sleep(1)
    print("GET EXCITED!\nLet's play Hangman!")


def display_rules():
    """
    Ask user if game rules are needed and display game rules as requested
    """
    print("\nBefore we start, would you like to see the "
          "instructions or are you good to go?")
    rules_on = input("Press y if yes, "
                     "or press enter to play the game:\n")
    if rules_on.lower() == "y":
        rules_txt()
        print("Are you ready to play?\n")
        input("Press enter to start the game >> \n")
    else:
        pass


def rules_txt():
    """
    Display game rules
    """
    print("\nHere are rules on how to play \n"
          "1. Select a category\n"
          "2. The amount of  displayed Underscores '_' hints\n"
          "   to the length of the word.\n"
          "3. You need to guess the word\n"
          "   by entering one letter at a time.\n"
          "4. If your answer is correct, the letter will be displayed\n"
          "   instead of the underscore'_'.\n"
          "5. If you guess all the letters and the word is complete,\n"
          "   you win the game\n"
          "6. If the incorrect letter is entered,\n"
          "   the hangman image will progress.\n"
          "   Space between the words is considered incorrect.\n"
          "7. If the number of incorrect attempts reaches the limit\n"
          "   and the hangman image completed the game ends.\n")


def category_select():
    """
    Prompt user to select a category for the game and validate the input
    """
    print("PLEASE CHOOSE ONE OF THE CATEGORY:\n")
    print("1. Countries, 2. Sports, 3. Animals", "4. Drinks\n",
          "5. All the category mixed\n")
    category_num = 0
    while not 1 <= category_num <= 5:
        try:
            category_num = int(input("Please enter 1, 2, 3, 4 or 5  >>>  \n"))
            if 1 <= category_num <= 5:
                return category_num
            else:
                pass
        except ValueError:
            print("Only number 1, 2, 3, 4 or 5 accepted")


def select_question():
    """
    Random word selection from the list and display _ for each letter
    """
    time.sleep(2)
    category_chosen = category_select()
    list_num = category_chosen - 1
    print(f"Category {category_chosen}  was chosen")
    if category_chosen == 5:
        category_item = random.choice(category)
    else:
        category_item = category[list_num]
        word = random.choice(category_item)
        return (word)


def hangman():
    """
    Main game function to display questions, check the answer
    and count attempts.
    Repeats process if game completion condition is not met.
    Either word completion or reaching full stages will end the game.
    """
    incorrect = 0   # Setting the starting point of incorrect attempts
    correct_guess = set([])   # Creating a empty list to store correct answers
    word = select_question()   # Random word chosen by the function
    check_answer = word.replace(" ", "")   # Removing space from answer
    answers = [i for i in check_answer]   # Create list from the word
    wrong_guess = []   # Incorrect letters goes in here
    while incorrect < stage_num:
        display_guess_message()
        """
        Print out _ for the remaining letters to guess
        """
        for i in word:
            if i == " ":
                print(i, end="  ")
            elif i in correct_guess:
                print(i.upper(), end=" ")
            else:
                print("_ ", end=" ")
        print('\n')
        guessed = input("Enter one letter! \n").lower()
        if guessed in answers:   # Checking the answer and determine the action
            if guessed in correct_guess:
                display_already_used()
                time.sleep(2)
            else:
                print(f"{guessed.upper()} is the right letter!")
                correct_guess.add(guessed)   # Add correct letter to the list
                word_letters = word.replace(" ", "")
                if correct_guess == set(word_letters):
                    print(f"CONGRATULATIONS!"
                          f"You have guessed the word {word.upper()}.")
                    # ASCII ART https://patorjk.com/software/taag
                    print("  _  _                         ")
                    print(" | || |_  _ _ _ _ _ __ _ _  _  ")
                    print(" | __ | || | '_| '_/ _` | || | ")
                    print(" |_||_|\_,_|_| |_| \__,_|\_, | ")
                    print("                         |__/  \n")
                    break
                time.sleep(2)
        else:
            if len(guessed) > 1:
                print("Enter only one letter at a time")
            else:
                print(f"' {guessed.upper()}' is the incorrect answer!")

            incorrect += 1   # Increment incorrect attempt
            print("\n".join(stages[:incorrect]))   # Display hangman image
            print("\n")
            wrong_guess.append(guessed.upper())
            print(f"Your incorrect guesses: {wrong_guess} ")
            time.sleep(2)
    if incorrect == stage_num:
        print(f"The answer is {word.upper()}")
        game_over()

    time.sleep(3)
    replay()


def display_guess_message():
    print("\n")
    print("Can you guess the word?")
    print("Enter one letter to see if you are right?")


def display_already_used():
    print("You have already used this letter before,"
          " it's already displayed!")


def game_over():
    """
    GAME OVER ASCII art
    """
    # ASCII ART https://patorjk.com/software/taag
    print("   ___                   ___              ")
    print("  / __|__ _ _ __  ___   / _ \__ _____ _ _ ")
    print(" | (_ / _` | '  \/ -_) | (_) \ V / -_) '_|")
    print("  \___\__,_|_|_|_\___|  \___/ \_/\___|_|  \n")
    

def replay():
    print("Would you like to play again?")
    print("Enter y or press RUN PROGRAM button above to play again.\n"
          "or press enter to exit the game.")
    play_again = input(
        "Please press y to play or press enter to exit the game\n")
    if play_again.lower() == "y":
        hangman()
    else:
        print("Hope you enjoyed the game!")


def main():
    display_title()  # print title function
    welcome()  # display user input name and greetings
    display_rules()  # display rules if user chooses
    hangman()  # main game function


main()
