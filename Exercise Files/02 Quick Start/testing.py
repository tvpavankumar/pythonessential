#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC

def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2, n):
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n // x))
            return False
    else:
           print(n, "is a prime number")
           return True


for a in range (1,20):
    isprime(a);
else :
    print("I am done");


def fullname(fname, lname) :
     print ("Full name is {} {}".format(fname,lname));

fullname("pavan","tummala")
