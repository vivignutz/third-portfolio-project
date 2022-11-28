#importing randomic words of the list words.txt
import random

def welcome_message():
    print("**********************************")
    print("***Welcome to the Hangman game!***")
    print("**********************************\n")
    print("Your goal is to guess the secret word.")
    print("You'll have to try one letter at a time.")
    print("If you hit the letter, it will be placed in the")
    print("word to bring you closer to getting it right.")
    print("If you miss, one part of your body will be hanged.\n")
    print("I wish you good luck!\n\n")
    """
    Function used to call the welcome message and instructions of the game. 
    """

def secret_word_loads():
    words = []
    with open("words.txt", "r", encoding="utf-8") as file:
      for line in file:
        line = line.strip()      #strip to take the blank spaces
        words.append(line)

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word
    print(secret_word)

    """
    Function opens randomically one secret word of the word.txt
    The append here adds a word from my list words.txt.

    and returns a random integer between 0 and the lenght of the word.
    I choose "upper" in order to turn the returned letters more visible.
    """


def initialize_hit_letters(word):
    return ["_" for letter in word]
"""
Function calls the chosen word and
places an empty space "_" for each word
"""


def asks_kick():
    kick = input("\n\nWhich letter do you wanny try?  \n\n")
    kick = kick.strip().upper()
    return kick
    """
    Requesting a letter kick.
    Upper used again for better visibility.
    """


def correct_kick(kick, right_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (kick == letter):
            right_letters[index] = letter
        index += 1 
        """
        To achieve a correct kick: if kick matches with a letter of the 
        secret word, this letter will be pushed from index.
        Index += >>>> it loops until match the same lenght of the word 
        """


def winner_message():
    print("\n\nCongratulations! You won!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    """
    This message will shows to the player in 
    case he kick all letters right and win the
    game.
    """


def loss_message(secret_word):
    print("\n\nOH NOOOO.... You lose!")
    print("\n\nThe word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
"""
This message will shows to the player in 
case he exhaust his kicks and the secret word
appears. The string .format(text) was used for that.
"""


def gallows(errors):
    print("  _______     ")
    print(" |/      |    ")

    if (errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
"""
The gallows is being designed acc. to the numbers of 
errors of the player. 7 wrong kicks can be done in total.
Simple functions print() were used to build gallows.
"""


def play():    #game sequence
  
    welcome_message()

    secret_word = secret_word_loads()

    right_letters = initialize_hit_letters(secret_word)

    hanged = False
    got_it = False
    errors = 0
    missing_letters = len(right_letters)

    print(right_letters)
    while (not got_it and not hanged):
      """
      While loop for "got-it" kicks and still remaining attempts
      """
    
      kick = asks_kick()

      if (kick in secret_word):
          correct_kick(kick, right_letters, secret_word)
          missing_letters = str(right_letters.count('_'))
          if (missing_letters == "0"): 
              print("\n\nCONGRATS!! You have found all the letters of '{}'".format(secret_word.upper()))
          """
          If the kick in secret_word is a correct kick inside of the secret_word
          and if the secret_word is complete, than print the message "CONGRATS..."
          """
        
        
      else:
          errors += 1
          print(right_letters)          
          print('\n\There are still {} letters left to match'.format(missing_letters))
          print('\n\nYou have {} attempts'.format(7 - errors))
          gallows(errors)
          """
          Otherwise, the right_letters are contabilized and subtracted
          from the maximal attempts (7).
          """

      hanged = errors == 7
      got_it = "_" not in right_letters


      print(right_letters)

    if (got_it):
        winner_message()
    else:
        loss_message(secret_word)

    print("\n\nEnd of the game")
    """

    """

if (__name__ == '__main__'):
    play()
