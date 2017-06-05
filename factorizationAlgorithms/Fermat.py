import math
import time

# overtime 15+15 cifre
# 150 secondi 10+10 cifre
# 0.020 secondi 5+5 cifre
# 1.001 *10^-5 3+3 cifre

# Check if n is a perfect square
def perfect_sqr(n):
    return n == int(math.sqrt(n)) ** 2

# Two primes p and q
p = 391281027997333
q = 403488712911637

p = 1500450271
q = 3267000013

p = 14401
q = 32377

p = 113
q = 181

# n to factorize
n =  p*q

# a is the ceiling of the square root of n
a = math.ceil(math.sqrt(n))

# Flags to exit the finding loop
found = False
overtime = False

b = 0

# "Timer start" to check the time of search
t0 = time.time()

# Until the loop can't find the solution or the search is gone too far
while not (found or overtime):

    # b^2 = a^2 - n ?
    b2 = pow(a,2)-n

    # check if b2 is a perfect square
    if perfect_sqr(b2):
        # if it is b is the square roots of b2 and we can exit from loop
        b = math.sqrt(b2)
        found = True
    else:
        # if it's not a is increased
        a = a+1
    if a > 1000000000000:
        # a is gone too far, stop the loop
        overtime = True
        print("Not found")

# "Timer end"
t1 = time.time()


if found:
    print("I found factorization:")
    print("Time waited: "+str(t1-t0)+" seconds\n")

    print("p = "+str(int(a-b)))
    print("q = "+str(int(a+b)))

else:
    print("N is too big for me")

