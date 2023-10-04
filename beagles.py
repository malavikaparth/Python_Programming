import random

NUM_DIGITS = 3 #Can be put to number of nay length
MAX_GUESSES = 10 #can be put to any number of tries

def main():
    print('''Bagels, a deductive logic game.
    By Malavika Parthasarathi with help of Al Sweigart al@inventwithpython.com
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say: That means:
    Pico One digit is correct but in the wrong position.
    Fermi One digit is correct and in the right position.
    Bagels No digit is correct.'''.format(NUM_DIGITS)) #This "format(NUM_DIGITS)" makes sure that "{}" is
                                                        #replaced by the number on NUM_DIGITS
    while True: #Main game loop.
        #Generate the secret number
        secret_num = getsecretnum()
        print("'I have thought up a number")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            #The input from the console
            input_guess = ''
            while len(input_guess) != NUM_DIGITS or not input_guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                input_guess = input(">")
            clue = getclue(input_guess, secret_num)
            print(clue)
            numGuesses += 1
            if input_guess == secret_num:
                print("You Won")
                break
            if numGuesses > MAX_GUESSES:
                print("Your chance is over")
                print("The secret code is",secret_num)
                break

        #Ask player if they want to play again.
        print("Wanna play again?")
        react = input("y>n?")
        if(react == 'n'):
            break

def getsecretnum():
    # Create a list of digits 0 to 9.
    numbers = list('0123456789')
    #shuffle the numbers
    random.shuffle(numbers)
    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretnum = ' '
    for i in range(0,NUM_DIGITS):
        secretnum += str(numbers[i])
    return secretnum

def getclue(input_guess, secret_num):
    #"Returns a string with the pico, fermi, bagels
    if input_guess == secret_num:
        return "You Won"
    clues = []
    for i in range(len(input_guess)):
        if input_guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif input_guess[i] in secret_num:
            clues.append('pico')

    if(len(clues) == 0):
            return "bagles"
    else:
        return clues



if __name__ == '__main__':
    main()