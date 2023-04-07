"""
All Imports
"""
import random
import time

# List of categories for guessing word
weather = ["climate", "isobar", "visibility",
           "showery", "unsettled", "rainbow"]
irish_names = ["caoimhe", "saoirse", "clodagh",
               "roisin", "eireann", "padraig", "tadhg"]
counties_of_ireland = ["limerick", "tipperary", "wexford",
                       "donegal", "longford", "galway", "dublin"]
drinks = ["tequila", "vermouth", "cognac",
          "whiskey", "water", "baileys"]

category = [weather, irish_names, counties_of_ireland, drinks]

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
    print("1. Weather, 2. Irish names, 3. Counties of Ireland", "4. Drinks\n",
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
        return(word)


def main():
    display_title()  # print title function
    welcome()  # display user input name and greetings
    display_rules()  # display rules if user chooses


main()
