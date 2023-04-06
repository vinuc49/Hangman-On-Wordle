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
  

def main():
    display_title()  # print title function
    welcome()  # display user input name and greetings
    

main()