import random
# importing randomic words of the list words.txt


def welcome_message():
    """
    Function used to call the welcome message, and
    instructions of the game.
    """
    print("\n\n**********************************")
    print("***Welcome to the Hangman game!***")
    print("**********************************\n")
    print("Here some information to you:\n")
    print("Your goal is to guess the secret word.")
    print("- You'll have to try one letter at a time.")
    print("- If you hit the letter right, it will be placed in the")
    print("word to bring you closer to getting all letters right.")
    print("- If you miss, one part of your body will be hanged.\n")
    print("I wish you good luck!\n\n")


def secret_word_loads():
    """
    Function opens randomically one secret word of the word.txt
    The append here adds a word from the list words.txt. and
    returns a random integer between 0 and the lenght of the word.
    I choose "upper" in order to turn the returned letters more visible.
    """
    words = []
    with open("words.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if len(line) > 0:
                words.append(line)

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def initialize_hit_letters(word):
    """
    Function calls the chosen word and
    places an empty space "_" for each word
    """
    return ["_" for letter in word]


def asks_kick():
    """
    Requesting a letter kick.
    Upper used again for better visibility.
    """
    while True:
        kick = input("\n\nWhich letter do you wanny try?  \n\n").strip()

        if (not kick.isalpha()) or len(kick) > 1:
            print("Please eenter a single letter.")
            continue

        #break

        kick = kick.upper()
        return kick


def correct_kick(kick, right_letters, secret_word):
    """
    To achieve a correct kick: if kick matches with a letter of the
    secret word, this letter will be pushed from index.
    Index += >>>> it loops until match the same lenght of the word
    """
    index = 0
    for letter in secret_word:
        if (kick == letter):
            right_letters[index] = letter
        index += 1


def winner_message():
    # This message will be showed to the player
    # in case he kick all letters right and win
    # the game.

    print("\n\nCONGRATULATIONS! YOU WON!!!")
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
    # This message will shows to the player in
    # case he exhaust his kicks and the secret word
    # appears. The string .format(text) was used for that.

    print("\n\nOH NOOOO.... YOU LOSE!!!")
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


def gallows(errors):
    # The gallows is being designed acc. to the numbers of
    # errors of the player. 7 wrong kicks can be done in total.

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


def play():
    """
    Missing_letters spaces have same lenght as
    right_letters of secret_word
    """
    # game sequence

    welcome_message()
    # calls the welcome_message

    secret_word = secret_word_loads()
    # secret_word loads

    right_letters = initialize_hit_letters(secret_word)

    hanged = False
    got_it = False
    errors = 0
    missing_letters = len(right_letters)

    print(right_letters)
    while (not got_it and not hanged):
        """
        While loop for "got-it" (right) kicks and
        still remaining attempts.
        """

        kick = asks_kick()

        if (kick in secret_word):
            """
            If the kick in secret_word is correct, and if the
            secret_word is complete, than print the message "YES!!..."
            """
            correct_kick(kick, right_letters, secret_word)
            missing_letters = right_letters.count('_')
            print(right_letters)

            if (missing_letters == "0"):
                print("\n\YES!! You have found all the letters of '{}'"
                    .format(secret_word.upper()))

        else:
            # Otherwise, the right_letters are contabilized and
            # subtracted from the maximal attempts (7).

            errors += 1
            print(right_letters)
            print('\n\nThere are still {} letters left to match'.format(missing_letters))
            print('\n\nYou have {} attempts'.format(7 - errors))
            gallows(errors)

        hanged = errors == 7
        got_it = "_" not in right_letters


    if (got_it):
        winner_message()
    else:
        loss_message(secret_word)

    print("\n\n*** END OF THE GAME ***\n\n")
    """
    "End of the game" will be printed in the end.
    """

    play_again = input(
        "Enter Y to play again or any other key to quit.").strip().upper()

    if play_again == 'Y':
        play()


if __name__ == '__main__':
    play()
    """
    calling multiple functions (all)
    in order to play the game
    """