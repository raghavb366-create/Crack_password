import sys, time, hashlib
from array import *
from .helperFunc import *
from . import totalguesses



def search_method_3(file_name,which_password):
    f = open(file_name)
    words = f.readlines()
    f.close
    number_of_words = len(words)
    for i in range(0, number_of_words):
        words[i] = cleanup(words[i])
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
            totalguesses.totalguesses += tests
            report_search_time(tests, time.time()-starttime)
            return True
        #else:
            #print ("Darn. " + ourguess_pass + " is NOT the password.")
        tests = tests + 1
        
        # Now let's try it with the first letter capitalized
        ourguess_pass = Cap(ourguess_pass)
        if (check_userpass(which_password, ourguess_pass)):
            print ("Success! Password  "+str(which_password)+" is " + ourguess_pass)
            tests += 1
            totalguesses.totalguesses += tests
            report_search_time(tests, time.time()-starttime)
            return True
        #else:
            #print ("Darn. " + ourguess_pass + " is NOT the password.")
        tests = tests + 1

    totalguesses.totalguesses += tests
    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return False