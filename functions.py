# Keith Brazill
# A function to square numbers.

#def square(x): 
  #  ans = x * x
   # return ans

#use def in python to define funtion, give function name(f),
#for f take input f(x) and carry out(:)
#return to define output (recipe for function)
#changed f to square as this is more descriptive of what
#funtion those, better practice.= x * x,
#added in "ans = x * x" statement now part of function
#changed return x * x to return ans
#(x) in round brackets is called an arguement, can have more than 1

# print(square(2)) #you can now use function 'f' anywhere in script

import math 
import functions

def power(a, b):
    ans = a
    b = b - 1
    while b > 0: 
        ans = ans * a
        b = b - 1
    return ans

print(power(3, 6))

def f(x):
    ans = x * x
    return ans
print(f(2))

def isprime(i):
      #Assume i is prime
    isprime = True 
    #Loop through only generated prime numbers faster than all number in 1st revision
    for j in range(2, math.floor(math.sqrt(i))):
        #See if j divides i
        if i % j == 0:
            # if it does i isn't prime and exit loop
            return False
    return True 
