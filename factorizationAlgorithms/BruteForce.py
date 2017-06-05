import math
import time

# overtime 15 + 15 cifre
# 245 secondi 10+10 cifre
# 0.002 secondi 5+5 cifre
# 1.71 * 10^-5 secondi 3+3 cifre


# Two primes p and q
p = 391281027997333
q = 403488712911637

p = 1500450271
q = 3267000013

p = 14401
q = 32377

#p = 113
#q = 181

# n to factorize
n =  p*q

# a is the ceiling of the square root of n
a = math.ceil(math.sqrt(n))

# Flags to exit the finding loop
found = False
overtime = False

i = 2

if n%i == 0:
    found = True
else:
    i = 3

# "Timer start" to check the time of search
t0 = time.time()

found = False

# Until the loop can't find the solution or the search is gone too far
while not found:
    if n%i==0:
        found = True
    else:
        i = i+2

# "Timer end"
t1 = time.time()

if i == n:
    print("n is prime")
else:
    print("I found factorization:")
    print("Time waited: "+str(t1-t0)+" seconds\n")

    print("p = "+str(i))
    print("q = "+str(int(n/i)))
