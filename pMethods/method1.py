import sys, time, hashlib
from array import *
from .helperFunc import MD5me, check_userpass, report_search_time, leading_zeroes
from . import totalguesses

# *** METHOD 1 ***
#
# search method 1 will try using digits as the password.
# first it will guess 0, 1, 2, 3...9, then it will try 00, 01, 02...99, etc.
def search_method_1(num_digits, which_password): # pass number in which_password , can define the rest in another file??
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
        if (check_userpass(which_password, ourguess)):
            print ("Success! Password "+str(which_password)+" is " + ourguess)
            still_searching = False   # we can stop now - we found it!
            result = True
        #else:
            #print ("Darn. " + ourguess + " is NOT the password.")
        a=a+1
    totalguesses.totalguesses += tests
    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result