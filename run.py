#importing randomic words of the list words.txt
import random

def print_welcome_message():
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
print_welcome_message()


def secret_word_loads():
  words = []
  with open("words.txt", "r", encoding="utf-8") as file:
    for line in file:
      line = line.strip() #strip retira espacos em branco
      words.append(line) #anexar uma pal. na linha

  number = random.randrange(0, len(words))
  secret_word = words[number].upper()
  return secret_word
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
  kick = input("\n\nWhich letter do you wanny try? ")
  kick = kick.strip().upper()
  return kick
"""
Requesting a letter kick.
Upper used again for better visibility.
"""


def correct_kick(kick, correct_letters, secret_word):
  index = 0
  for letter in secret_word:
    if (kick == letter):
      right_letters[index] = letter
    index += 1 #(index = index + 1) to loop until the same lenght of the word


def winner_message():
  print("Congratulations! You won!!!")
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


def loss_message(secret_word):
  print("BOAAAAAH.... You lose!")
  print("The word was {}".format(secret_word))
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