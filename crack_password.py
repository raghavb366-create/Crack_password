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

# Ask the user if they want the onscreen instructions
yesno = input("Do you want the program to pause at each step so you have time to read the instructions? (type yes or no): ")
if yesno == "no" or yesno == "n" or yesno == "NO" or yesno == "N":
    show_instructions = False
    print("Okay, then once you start the program it will run without pausing.")
else:
    show_instructions = True
    print("Okay, the program will display more information as it runs and pause at each step.")
    input("Press enter to continue.")
    
#--------------- global variables we expect will be used by any function -----------
#
# a number from 1 to 6 selects which password we'll be trying to guess from
# a selection below.
which_password = 0

# the user names and password we're trying to 'crack'.
# IMPORTANT: do not try to enter passwords to "guess" here! This part of the code
# is just initializing the variables. Scroll down to the "main" function at the bottom
# of the program, where you can edit password0 to test out different algorithms.
# The other passwords (1-6) were created by Science Buddies and "hidden" using
# something called hashing. This prevents you from "cheating" by knowing the
# password in advance. Read the project's procedure for more details about how hashing works.

password0 = "" # remember, do not edit password0 here! scroll down to the "main" function!
password1 = ""
password2 = ""
password3 = ""
password4 = ""
password5 = ""
password6 = ""


# total number of guesses we had to make to find it
totalguesses = 0



#--------------- extra helper functions -------------------
# These will be used by our search routines later on. We'll get these defined and out
# of the way. The actual search program is called "main" and will be the last one
# defined. Once it's defined, the last statement in the file runs it.
#

## Convert a string into MD5 hash
def MD5me(s):
    result = s.encode("utf-8") #Raghav - Converts a string into a sequence of bytes using UTF-8 encoding
    result = hashlib.md5(result).hexdigest() #Raghav - Turns this sequence of bytes into a MD5 hash object, then returns it as a hexadecimal string.
    return result

# Takes a number from 0 on up and the number of digits we want it to have. It uses that
# number of digits to make a string like "0000" if we wanted 4 or "00000" if we wanted
# 5, converts our input number to a character string, sticks them together and then returns
# the number we started with, with extra zeroes stuck on the beginning, maxing out on the. 
def leading_zeroes(n, length):
    t=("0"*length)+str(n)
    t=t[-length:] #Raghav - Adds 0's behind the current string n until it reaches length.
    return t

# This function checks if the MD5 hash value of the password you have guessed equals
# the MD5 hash value of the real password.
def check_userpass(which_password, password):
    global password0, password1, password2, password3
    global password4, password5, password6
    
    result = False
    match which_password:
        case 0:
            if password == password0:
                result = True
        case 1:
            if MD5me(password) == password1:
                result = True
        case 2:
            if (MD5me(password) == password2):
                result = True
        case 3:
            if (MD5me(password) == password3):
                result = True
        case 4:
            if (MD5me(password) == password4):
                result = True
        case 5:
            if (MD5me(password) == password5):
                result = True
        case 6:
            if (MD5me(password) == password6):
                result = True
            
    return result

# This displays the results of a search including tests per second when possible
def report_search_time(tests, seconds):
    if (seconds > 0.000001):
        print ("The search took "+make_human_readable(seconds)+" seconds for "+make_human_readable(tests)+" tests or "+make_human_readable(tests/seconds)+" tests per second.")
    else:
        print ("The search took "+make_human_readable(seconds)+" seconds for "+make_human_readable(tests)+" tests.")
    return

# This function takes in numbers, rounds them to the nearest integer and puts
# commas in to make it more easily read by humans
def make_human_readable(n):
    if n>=1:
        result = ""
        temp=str(int(n+0.5))
        while temp != "":
            result = temp[-3:] + result
            temp = temp[:-3]
            if temp != "":
                result = "," + result
    else:
        temp = int(n*100)
        temp = temp /100
        result = str(temp)
    return result
        
## A little helper program to remove any weird formatting in the file
def cleanup (s):
    s = s.strip()
    return s
# Opened file - Raghav, just opening the file in one place rather than in method 3 or 4 each time.
f = open("passwords.txt")
words = f.readlines()
f.close
number_of_words = len(words)
for i in range(0, number_of_words):
        words[i] = cleanup(words[i])

## A little helper program that capitalizes the first letter of a word
def Cap (s):
    s = s.upper()[0]+s[1:]
    return s

# --------------------- password guessing functions ----------------------------

# *** METHOD 1 ***
#
# search method 1 will try using digits as the password.
# first it will guess 0, 1, 2, 3...9, then it will try 00, 01, 02...99, etc.
def search_method_1(num_digits):
    global totalguesses
    result = False
    a=0
    #num_digits = 3    # How many digits to try. 1 = 0 to 9, 2 = 00 to 99, etc.
    starttime = time.time()
    tests = 0
    still_searching = True
    print()
    print("Using method 1 and searching for "+str(num_digits)+" digit numbers...")
    while still_searching and a<(10**num_digits):
        ourguess = leading_zeroes(a,num_digits)
        # uncomment the next line to print each guess, this can help with debugging
        # print(ourguess)
        tests = tests + 1
        totalguesses = totalguesses + 1
        if (check_userpass(which_password, ourguess)):
            print ("Success! Password "+str(which_password)+" is " + ourguess)
            still_searching = False   # we can stop now - we found it!
            result = True
        #else:
            #print ("Darn. " + ourguess + " is NOT the password.")
        a=a+1

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result

# *** OPTIMIZED METHOD 2 - Raghav ***
#
# Search method 2 is a brute force using itertools, essentially looping through
# characters from the wheel until it reaches the upper limit of the characters
# given. Quicker than the original because of itertools product.

def search_method_2(num_pass_wheels):
    global totalguesses
    
    print(f"\nUsing optimized method 2 with {num_pass_wheels} characters.")
    
    #Using a tuple for faster access than a string.  It is a constant so all caps
    WHEEL = tuple(" ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
    
    starttime = time.time()
    tests = 0
  
    for combination in product(WHEEL, repeat=num_pass_wheels): #Product is part of a library, and it allows for a faster iteration.
         # Skip empty password if first char is space
        combination = combination[::-1] # Reverses the tuple because Product always generates at the end of one.
        if combination[0] == ' ':
            continue
        combination = filter(str.strip,combination) # gets rid of the whitespace inside of the tuple, and leaves the characters there.
        ourguess_pass = ''.join(combination) #Makes the tuple into a string to pass.
        if (check_userpass(which_password, ourguess_pass)):
            print ("Success! Password  "+str(which_password)+" is " + ourguess_pass)
            tests += 1
            report_search_time(tests, time.time()-starttime)
            return True
          
        tests += 1
    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return False

# *** METHOD 3 *** - Optimized by Raghav, got rid of opening the file here, moved it elsewhere
# Made the code use less loops.
#
# search method 3 uses a list of dictionary words. In this case, we have a list
# of the 500 most commonly used passwords in 2005 as collected by Mark Burnett
# for his book "Perfect Passwords" (ISBN 978-1597490412). Because the list comes
# from so many people around the world, we had to remove some of the passwords.
# People like to use passwords that they think will shock other people, so
# sometimes they're not fit for polite company.
def search_method_3(file_name):
    global totalguesses
    global words
    global number_of_words
  
    print()
    print("Using method 3 with a list of "+str(number_of_words)+" words...")
    # Let's try each one as the password and see what happens
    starttime = time.time()
    tests = 0

    for word in words:
        ourguess_pass = word
        # uncomment the next line to print the current guess
        # print("Guessing: "+ourguess_pass)
        # Try it the way it is in the word list
        if (check_userpass(which_password, ourguess_pass)):
            print ("Success! Password  "+str(which_password)+" is " + ourguess_pass)
            tests += 1
            report_search_time(tests, time.time()-starttime)
            return True
        #else:
            #print ("Darn. " + ourguess_pass + " is NOT the password.")
        tests = tests + 1
        totalguesses = totalguesses + 1
        # Now let's try it with the first letter capitalized
        ourguess_pass = Cap(ourguess_pass)
        if (check_userpass(which_password, ourguess_pass)):
            print ("Success! Password  "+str(which_password)+" is " + ourguess_pass)
            tests += 1
            report_search_time(tests, time.time()-starttime)
            return True
        #else:
            #print ("Darn. " + ourguess_pass + " is NOT the password.")
        tests = tests + 1
        totalguesses = totalguesses + 1

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return False

# *** OPTIMIZED METHOD 4 *** - Raghav    
# Search method 4 is similar to 3 in that it uses the dictionary, but it tries two
# two words separated by a punctuation character.
def search_method_4(file_name):
    global totalguesses
    global words
    global number_of_words

    # Let's try each one as the password and see what happens
    starttime = time.time()
    tests = 0
    still_searching = True
    
    PUNCTUATION = tuple("~!@#$%^&*()_-+={}[]:<>,./X ")  # X is a special case where we omit
                                              # the punctuation to run the words together

    print()
    print("Using Optimized method 4 with "+str(len(PUNCTUATION))+" punctuation characters and "+str(number_of_words)+" words...")


    for combination in product(words,PUNCTUATION,words): #Using itertools to create a combination of two words
                                                         #separated by one piece of punctuation.
        if combination[1] == "X": #If the punctuation is X, gets rid of the space between the two words.
            combination = [combination[0],combination[2]]
        ourguess_pass = ''.join(combination) #Makes the words into a string.
        if (check_userpass(which_password, ourguess_pass)):
            print ("Success! Password  "+str(which_password)+" is " + ourguess_pass)
            tests += 1
            report_search_time(tests, time.time()-starttime)
            return True
        # Checks the word and returns True if guessed correctly.
     
        tests += 1

    seconds = time.time()-starttime
    print(seconds)
    report_search_time(tests, seconds)
    return False


# -------------------------- main function ----------------------------

def main(argv=None):
    global password0, password1, password2, password3
    global password4, password5, password6, totalguesses
    global which_password

    # To test your own algorithms, change password0. This password is displayed
    # in "plaintext" so you can see the password in advance. 
    password0 = "qwerty123456"
    
    # These are the passwords created by Science Buddies for you to try and crack.
    # Their real text is hidden from you using something called MD5 hashing. This converts
    # the original password to a block of (seemingly) gibberish text. 
    # You can create your own MD5 hashes using the MD5me function in this program.
    # For example, the code
    # password7=MD5me("ScienceBuddies")
    # will set password7 equal to the MD5 hash value of "Science Buddies"
    #
    # Do NOT edit these hash values if you want to try and guess the passwords
    # that were pre-set by Science Buddies. The example code will automatically guess
    # passwords 1-5, so you can use them to understand how the different search methods work.
    # It will not automatically guess password 6. You will need to make some changes to the
    # existing methods or come up with your own algorithm to guess password 6.
    password1="202cb962ac59075b964b07152d234b70"
    password2="570a90bfbf8c7eab5dc5d4e26832d5b1"
    password3="f78f2477e949bee2d12a2c540fb6084f"
    password4="09408af74a7178e95b8ddd4e92ea4b0e"
    password5="2034f6e32958647fdff75d265b455ebf"
    password6="9b3af42d61cde121f40b96097fb77d3e"

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
        foundit = search_method_3("passwords.txt")
    # Still looking? Let's combine the common passwords 2 at a time
    if not foundit:
        print("Method 3 did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_4("passwords.txt")
    # Still looking? See if it's a single digit
    if not foundit:
        print("Method 4 did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_1(1)
    # Still looking? See if it's a 2 digit number
    if not foundit:
        print("Method 1 (1 digit) did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_1(2)
    # Still looking? See if it's a 3 digit number
    if not foundit:
        print("Method 1 (2 digit) did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_1(3)
    # Still looking? See if it's a 4 digit number
    if not foundit:
        print("Method 1 (3 digit) did not work!")
        if show_instructions:
            input("Press enter to continue.")
        foundit = search_method_1(4)
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
        print ("The total search for all methods took "+make_human_readable(seconds)+" seconds and "+make_human_readable(totalguesses)+" guesses.")
        print ("(on some machines, Python doesn't know how long things actually took)")
    else:
        print ("The total search for all methods took "+make_human_readable(seconds)+" seconds and "+make_human_readable(totalguesses)+" guesses.("+make_human_readable(totalguesses/seconds)+" guesses per second)")
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

