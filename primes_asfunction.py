# Keith Brazill
# Computing the Primes

import math 

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

#My list of primes - TBD.
P = [] 

#Loop through all numbers in range and check if prime/not prime

for i in range(2, 1000):
  
    # If it is prime, then append to P
    if isprime(i):
       P.append(i)     

#Print the list
print(P)     