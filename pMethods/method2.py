import sys, time, hashlib
from array import *
from .helperFunc import *
from itertools import product
from . import totalguesses

def search_method_2(num_pass_wheels,which_password):
    
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
            totalguesses.totalguesses += tests
            report_search_time(tests, time.time()-starttime)
            return True
          
        tests += 1
    totalguesses.totalguesses += tests
    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return False