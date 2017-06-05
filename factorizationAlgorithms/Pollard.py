import math
import time

# 23 secondi 15+15 cifre
# 0.06 secondi 10+10 cifre
# 5*10^-4 secondi 5+5 cifre
# 1.12*10^-5 secondi 3+3 cifre



def g(x,n):
    return (x**2 + 1)%n

# Two primes p and q
p = 391281027997333
q = 403488712911637

#p = 1500450271
#q = 3267000013

#p = 14401
#q = 32377

#p = 113
#q = 181


# n to factorize
n =  p*q


x = 2
y = 2
d = 1

# "Timer start" to check the time of search
t0 = time.time()

while (d == 1):
    x = g(x,n)
    y = g(g(y,n),n)
    d = math.gcd(abs(x - y), n)

# "Timer end"
t1 = time.time()

if d == n:
    print("I cannot reach the factorization")
else:
    print("I found factorization:")
    print("Time waited: "+str(t1-t0)+" seconds\n")

    print("p = "+str(d))
    print("q = "+str(int(n/d)))