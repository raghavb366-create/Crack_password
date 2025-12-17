#!/usr/bin/python

# Written by Howard Eglowstein, Science Buddies, 2014
# Updated by Ben Finio, Science Buddies, 2017
# formatting bugs fixed, 11/13/17

# This program is offered for use with the Science Buddies project idea
# "How Easily Can Your Password Be Hacked?" which lets you explore the
# makeup of a good password. This program will help you understand some
# methods that people use to guess other people's passwords. To see detailed written
# instructions for this project, visit
# https://www.sciencebuddies.org/science-fair-projects/project-ideas/CompSci_p046/computer-science/password-security-how-easily-can-your-password-be-hacked
# If you use this program, or a modified version of it, for a science project,
# make sure to credit Science Buddies. Using somebody else's code without giving
# them credit is plagiarism, just like if you copied their writing.
# You'll notice that several parts of the code have places where 
# print() functions have been turned into comments. You might want to uncomment
# these print statements when debugging your program (or add more of your own in
# other places), but they will make your program run slower. There are also many lines
# that pause the program using input() statements. This gives you a chance to read
# the output and understand how the program works. Once your program is
# working, you can comment out these print() and input() statements to make it run faster.

#Tell Python we want to use some functions it doesn't always use
import sys, time, hashlib
from array import *
from itertools import product
from pMethods.helperFunc import *
from pMethods.method1 import search_method_1
from pMethods.method2 import search_method_2
from pMethods.method3 import search_method_3
from pMethods.method4 import search_method_4
import pMethods.totalguesses as totalguesses
import password0



# -------------------------- main function ----------------------------

def main(argv=None):

    # # To test your own algorithms, change password0. This password is displayed
    # # in "plaintext" so you can see the password in advance. 
    # password0 = "qwerty123456"
    
    # # These are the passwords created by Science Buddies for you to try and crack.
    # # Their real text is hidden from you using something called MD5 hashing. This converts
    # # the original password to a block of (seemingly) gibberish text. 
    # # You can create your own MD5 hashes using the MD5me function in this program.
    # # For example, the code
    # # password7=MD5me("ScienceBuddies")
    # # will set password7 equal to the MD5 hash value of "Science Buddies"
    # #
    # # Do NOT edit these hash values if you want to try and guess the passwords
    # # that were pre-set by Science Buddies. The example code will automatically guess
    # # passwords 1-5, so you can use them to understand how the different search methods work.
    # # It will not automatically guess password 6. You will need to make some changes to the
    # # existing methods or come up with your own algorithm to guess password 6.
    # password1="202cb962ac59075b964b07152d234b70"
    # password2="570a90bfbf8c7eab5dc5d4e26832d5b1"
    # password3="f78f2477e949bee2d12a2c540fb6084f"
    # password4="09408af74a7178e95b8ddd4e92ea4b0e"
    # password5="2034f6e32958647fdff75d265b455ebf"
    # password6="9b3af42d61cde121f40b96097fb77d3e"


    # Ask the user if they want the onscreen instructions
    yesno = input("Do you want the program to pause at each step so you have time to read the instructions? (type yes or no): ")
    if yesno == "no" or yesno == "n" or yesno == "NO" or yesno == "N":
        show_instructions = False
        print("Okay, then once you start the program it will run without pausing.")
    else:
        show_instructions = True
        print("Okay, the program will display more information as it runs and pause at each step.")
        input("Press enter to continue.")
        
    # start searching
    which_password = 1
    if show_instructions:
        print()
        print("Did you read the instructions on the Science Buddies website yet?")
        print("How about the comments in the program?")
        print("Make sure you read those instructions before you continue!")
        input("Press enter to start the program.")
        print()
        print("This program will use several different algorithms to try and guess passwords.")
        print("You can set password 0 yourself (see comments in program).")
        print("Passwords 1-6 are pre-set by Science Buddies and hidden from you.")
        print("The example code will automatically guess passwords 1-5.")
        print("It will not guess password 6 unless you make some changes to the code.")
        print()

    # Raghav - Try catch for if the user enters a number outside of the range or enters in a non integer
    while True:
        try:
            which_password = int(input("Which password do you want to try to guess (0-6)? "))
            if not(which_password <=6 and which_password >= 0):
                print("Enter an integer from 0-6")
                continue
            break
        except ValueError:
            print("Invalid input, input an integer from 0-6")
    if 6 == which_password and show_instructions:
        print()
        print("WARNING: The example code will NOT guess password 6 on its own!")
        print("You will need to come up with your own algorithm to guess password 6.")
        print("Try changing password 0 in the program and using it to test your own algorithms.")
        input("Press ctrl+C if you need to stop the program, or press enter to continue.")
    if show_instructions:
        print()
        print("The program will now automatically try to guess the password using several different methods:")
        print()
        print("Method 1 will only guess digits 0-9.")
        print("Method 2 will guess digits 0-9 as well as letters a-z and A-Z.")
        print("Method 3 will guess using a list of common passwords.")
        print("Method 4 will try combinations of common words with punctuation in between them.")
        print("(we will not try the methods in this order though - can you guess why?)")
        print()
        print("Read the comments in the code for more details about each method.")
        input("Press enter to continue.")
        print()
    
    overallstart = time.time()
    foundit = False
    print("Trying to guess password "+str(which_password)+"...")
    # Look through our list of common passwords first
    if not foundit:
        foundit = search_method_3("passwords.txt",which_password)
    # Still looking? Let's combine the common passwords 2 at a time
    if not foundit:
        print("Method 3 did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_4("passwords.txt",which_password)
    # Still looking? See if it's a single digit
    if not foundit:
        print("Method 4 did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_1(1,which_password)
    # Still looking? See if it's a 2 digit number
    if not foundit:
        print("Method 1 (1 digit) did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_1(2,which_password)
    # Still looking? See if it's a 3 digit number
    if not foundit:
        print("Method 1 (2 digit) did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_1(3,which_password)
    # Still looking? See if it's a 4 digit number
    if not foundit:
        print("Method 1 (3 digit) did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_1(4,which_password)
    # Still looking? Use our rotary wheel simulation up to 6 wheels.
    # This should take care of any 5 digit number as well as letter
    # combinations up to 6 characters
    if not foundit:
        print("Method 1 (4 digit) did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_2(4)
    # Still looking? Try 7 digit numbers
    if not foundit:
        print("Method 2 (6 digits) did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_1(7)
    # Still looking? Try 8 digit numbers
    if not foundit:
        print("Method 2 (7 digits) did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_1(8)
    seconds = time.time()-overallstart
    # When testing this project, some users reported that the next lines of code reported
    # an error when Python tried to divide by zero. On those machines, the clock seems
    # to think that the seconds calculation just above gave us "zero" seconds which doesn't
    # make any sense. To avoid the crash though, we'll test for that case and avoid the
    # problem.
    print()
    if (seconds < 0.00001):
        print ("The total search for all methods took "+make_human_readable(seconds)+" seconds and "+make_human_readable(totalguesses.totalguesses)+" guesses.")
        print ("(on some machines, Python doesn't know how long things actually took)")
    else:
        print ("The total search for all methods took "+make_human_readable(seconds)+" seconds and "+make_human_readable(totalguesses.totalguesses)+" guesses.("+make_human_readable(totalguesses.totalguesses/seconds)+" guesses per second)")
    print()
    if foundit:
        if (6 == which_password):
            print("Wow! Be sure to confirm your find at http://www.sciencebuddies.org/science-fair-projects/project_ideas/CompSci_p046/PasswordCrack.shtml")
        elif (0 == which_password):  # The Science Buddies website can't confirm passwords you added yourself
            print ("Your algorithm correctly guessed the password you entered. Try some others or see if you can make it guess faster.")
        else:
            print("You can confirm your find at http://www.sciencebuddies.org/science-fair-projects/project_ideas/CompSci_p046/PasswordCrack.shtml")

print ("Science Buddies: How Easily Can Your password Be Hacked?")
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

