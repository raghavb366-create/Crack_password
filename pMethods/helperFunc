import sys, time, hashlib
from array import *

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