import sys, time, hashlib
from itertools import product
from array import *
from .helperFunc import *
from . import totalguesses



def search_method_4(file_name,which_password):
    f = open(file_name)
    words = f.readlines()
    f.close
    number_of_words = len(words)
    for i in range(0, number_of_words):
        words[i] = cleanup(words[i])

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
            totalguesses.totalguesses += tests
            report_search_time(tests, time.time()-starttime)
            return True
        # Checks the word and returns True if guessed correctly.
     
        tests += 1
    totalguesses.totalguesses += tests
    seconds = time.time()-starttime
    print(seconds)
    report_search_time(tests, seconds)
    return False
