# -*- coding: utf-8 -*-
"""
Created on Tue Jul 09 16:50:48 2019

@author: nathan.curtis
"""
import random
play = "y"
while play == "y":
    cows = 0
    bulls = 0
    # generate a random 4-digit number with no repeated digits
    number = random.sample(range(10), 4)
    # ask user for guess and check validity, loop until valid guess is made
    valid = 0
    while valid == 0:
        guess = raw_input("Guess a number: ")
        # convert guess to an array
        guessarray = [int(x) for x in str(guess)]
        check = set(guessarray)
        if len(check) < len(guessarray) or len(guessarray) != 4:
            print "Number invalid, must be 4 unique digits"
        else:
            valid = 1
            guesses = 1
    while bulls != 4:
        # compare each digit of the guess with each digit of the number
        for i in range(4):
            for j in range(4):
                if guessarray[i] == number[j]:
                    if i == j:
                        bulls += 1
                    else:
                        cows += 1                    
        # return guessarrayults
        print "Cows: " + str(cows) + " Bulls: " + str(bulls)
        if bulls == 4:
            print str(guess) + " is correct. Great job! You got it in " \
            + str(guesses) + " guesses."
            play = raw_input("Play again? (y/n) ")
        else:
            cows = 0
            bulls = 0
            valid = 0
            while valid == 0:
                guess = raw_input("Guess again: ")
                guessarray = [int(x) for x in str(guess)]
                check = set(guessarray)
                if len(check) < len(guessarray) or len(guessarray) != 4:
                    print "Number invalid, must be 4 unique digits"
                else:
                    valid = 1
                    guesses += 1

