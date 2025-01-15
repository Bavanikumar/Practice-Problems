##Given a non-negative integer n. The task is to check if it is a power of 2.

def isPowerofTwo(n):
      # code here
      while n%2 == 0:
          n=n/2
      return n == 1 # Returns True if n is 1

#Logic::
# Repeatedly divide n with 2 , The first time when you get an non-zero remainder you know n is not an power of 2.
# you can modify this logic into checking power other than 2 (replace 2 by that number)
