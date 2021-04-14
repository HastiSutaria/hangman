import random
def hangman():
    
    word = random.choice(["laptop", "life", "earth", "zebra", "xmastree","bank", "pencil", "orange", "coding", "python", "hangman", "set"])
    valid_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    turn = 10
    guessmade = ''

    while len(word)>0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + ""
        if main == word:
            print(main)
            print("HURRAY", name , "you win the game. ")
            print("You saved the kind man!")
            break
        print("guess the word: ", main)
        guess = input()
        
        if guess in valid_letters:
            guessmade = guessmade+guess
        else:
            print("Enter the valid alphbetical character.")
            guess=input()
        if guess not in word:
            turn = turn - 1
        
            if turn == 9:
                print("9 turns left.")
                print("   ----------   ")
            if turn == 8:
                print("8 turns left.")
                print("   ----------   ")
                print("       O        ")
            if turn == 7:
                print("7 turns left.")
                print("   ----------   ")
                print("       O        ")
                print("       |        ")
            if turn == 6:
                print("6 turns left.")
                print("   ----------   ")
                print("       O        ")
                print("       |        ")
                print("      /         ")
            if turn == 5:
                print("5 turns left.")
                print("   ----------   ")
                print("       O        ")
                print("       |        ")
                print("      / \       ")
            if turn == 4:
                print("4 turns left.")
                print("   ----------   ")
                print("     \ O        ")
                print("       |        ")
                print("      / \       ")
            if turn == 3:
                print("3 turns left.")
                print("   ----------   ")
                print("     \ O /      ")
                print("       |        ")
                print("      / \       ")
            if turn == 2:
                print("2 turns left.")
                print("   ----------   ")
                print("     \ O / |    ")
                print("       |        ")
                print("      / \       ")
            if turn == 1:
                print("Only 1 turn left.")
                print("Last breaths. Take care!")
                print("   ----------   ")
                print("     \ O /_|    ")
                print("       |        ")
                print("      / \       ")
            if turn == 0:
                print("   ----------   ")
                print("       O_|      ")
                print("      /|\       ")
                print("      / \       ")
                print("You lost! You just killed the kind man!")
                break



name = input("Hi! What is your name?")
print("Welcome", name, "! Let's play hangman.")
print("--------------------------------------")
print("Try to guess the word in 10 attempts by saving a kind man or you will let the kind man die!")
print("-------------------------------------------------------------------------------------------")
hangman()
print()