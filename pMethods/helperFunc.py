import sys, time, hashlib
from array import *

password0 = "qwerty123456"
password1="202cb962ac59075b964b07152d234b70"
password2="570a90bfbf8c7eab5dc5d4e26832d5b1"
password3="f78f2477e949bee2d12a2c540fb6084f"
password4="09408af74a7178e95b8ddd4e92ea4b0e"
password5="2034f6e32958647fdff75d265b455ebf"
password6="9b3af42d61cde121f40b96097fb77d3e"


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
def Cap (s):
    s = s.upper()[0]+s[1:]
    return s
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