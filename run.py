"""
All Imports
"""
import random
import time


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


def main():
    display_title()  # print title function
    welcome()  # display user input name and greetings
    display_rules()  # display rules if user chooses


main()
