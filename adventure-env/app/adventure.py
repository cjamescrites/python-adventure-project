import time
import logging

# For Python 3.9 or newer
# logging.basicConfig(filename='playerchoices.log', encoding='utf-8', level=logging.DEBUG)

# For Python3.8 or older
root_logger= logging.getLogger()
root_logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('playerchoices.log', 'w', 'utf-8')
handler.setFormatter(logging.Formatter('%(name)s %(message)s'))
root_logger.addHandler(handler)

class Character:
    def __init__(self, letter, type, primary_weapon, secondary_weapon):
        self.letter = letter
        self.type = type
        self.primary_weapon = primary_weapon
        self.secondary_weapon = secondary_weapon
  
    def describe_character(self):
        print(f"                                  {self.letter} I am a {self.type}, and I use a {self.primary_weapon} and a {self.secondary_weapon}.")

archer = Character("1.", "Archer", "Bow", "Arrow")
bard = Character("2.", "Bard", "Guitar", "Voice")
swordsman = Character("3.", "Swordsman", "Sword", "Shield")

# Function handling the first input choice in the game
def character_selection():
    choice = input("                                  Select a character by number... ")
    choosing = True
    logging.info('Player is prompted for character selection')
    while choosing == True:
        if choice == "1":
            global character
            character = "Archer"
            logging.info('Player has chosen Archer character')
            choosing = False
        elif choice == "2":
            character = "Bard"
            logging.info('Player has chosen Bard character')
            choosing = False
        elif choice == "3":
            character = "Swordsman"
            logging.info('Player has chosen Swordsman character')
            choosing = False
        else:
            print("                       That adventurer does not exist... please select 1, 2, or 3!")
            logging.info('Player has made an invalid character selection')
            character_selection()
        return    

# Function handling the second input choice in the game
def fork_choice():
    choice = int(input("                                         Please select a number... "))
    logging.info('Player is prompted first progression choice')
    choosing = True
    while choosing == True:
        if choice == 1:
            global first_decision
            first_decision = "the foggy path where visibility is limited"
            global first_consequence
            first_consequence = False
            logging.info('Player has chosen foggy path choice')
            choosing = False
        elif choice == 2:
            first_decision = "the wooded path leading to a small village"
            logging.info('Player has chosen wooded path choice')
            first_consequence = True
            choosing = False
        else:
            print(" ")
            print("                                   Please select a valid number... 1 or 2.")
            logging.info('Player has made an invalid choice')
            fork_choice()
        return

# Function handling the consequence of the second input choice in the game
def choice_outcome():
    if first_consequence == False:
        logging.info('Player is prompted about approaching a beast')
        print(" ")
        time.sleep(2)
        print("                                                 As you make your way down the foggy")
        print(" ")
        time.sleep(2)
        print("                              You noticed a strange sounds ahead seeming to come from a feral beast")
    else:
        logging.info('Player has passed out due to an unknown gas')
        print(" ")
        print("                                            As you make your way down this path...")
        print(" ")
        time.sleep(2)
        print("                                       You being to smell a strong odor resembling sulfur")
        print(" ")
        time.sleep(2)
        print("                                      Your vision begins to get blurry and you pass out")
        print(" ")
        time.sleep(2)
        print("                                     You awaken some how back at the fork in the road....")
        print(" ")
        time.sleep(2)
        print("                      Do you wish to traverse the 1) foggy path or make another attempt at the 2) wooded path?")
        print(" ")
        time.sleep(2)
        fork_choice()
        choice_outcome()

# Function handling the final input choice in the game
def final_choice():
    logging.info('Player is prompted with a choice of how he will approach the beast')
    choice = int(input("                                         Please decide now... "))
    choosing = True
    while choosing == True:
        if choice == 1:
            logging.info('Player draws his weapon, beast is scared away')
            print(" ")
            time.sleep(2)
            print("                                    You draw your weapon, the sound you make scares the beast")
            print(" ")
            time.sleep(2)
            print("                                     The monster runs passed you, revealing itself to be just a deer")
            choosing = False
        elif choice == 2:
            logging.info('Player sneaks passed the beast')
            print(" ")
            time.sleep(2)
            print("                                You sneak past the beast quietly without catching a glimpse of the monster")
            choosing = False
        else:
            print(" ")
            print("                                                                 Please choose 1 or 2 ")
            final_choice()
        return

# Actual Game that prompts in the terminal with logging and time functions added.
logging.info('Game has started')
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
print(".:|:.                                                                                                           .:|:.")
print(".:|:.    Hello there adventurer! A treachous journey awaits you... Please decide how you wish to proceed...     .:|:.")
print(".:|:.                                                                                                           .:|:.")
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
print(" ")
time.sleep(2) 
archer.describe_character()
print(" ")
time.sleep(2) 
bard.describe_character()
print(" ")
time.sleep(2) 
swordsman.describe_character()
print(" ")
time.sleep(2) 
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
print(" ")
character_selection()
print(" ")
time.sleep(1) 
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
print(" ")
print(f"                                   Wise choice adventurer! You seem like a {character}.")
print(" ")
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
time.sleep(1) 
print(" ")
print("                                             Let us begin our adventure!")
print(" ")
time.sleep(2) 
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
time.sleep(1) 
print(" ")
print("                                     You approach fork in the road...")
print(" ")
time.sleep(2)
print("                                 One way is a foggy path, visibility is limited")
print(" ")
time.sleep(2)
print("                                 The other way wooded path leading a small village")
print(" ")
time.sleep(2)
print("                         How do you wish to proceed? 1) Foggy path or  2) Small village path?")
print(" ")
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
print(" ")
time.sleep(1)
fork_choice()
print(" ")
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
print(" ")
time.sleep(2)
print(f"                                        You have decided to go down {first_decision}")
print(" ")
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
print(" ")
choice_outcome()
time.sleep(2)
print(" ")
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
print(" ")
time.sleep(2)
print("                                                Do you 1) draw your weapon or 2) attempt to sneak?")
print(" ")
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
print(" ")
time.sleep(2)
final_choice()
print(" ")
logging.info('Player makes it to a harbor, and is ready to begin his next adventure')
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
print(" ")
time.sleep(2)
print("                                                         As you continue down the path")
print(" ")
time.sleep(2)
print("                                                         The fog begins to clear...")
print(" ")
time.sleep(2)
print(" ")
print("                                  The path leads you to a harbor with a ship waiting for you")
time.sleep(2)
print(" ")
print("                                Where the ship takes you... we will have to see at a later time.....")
print(" ")
print(".:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.:|:.")
print(" ")
