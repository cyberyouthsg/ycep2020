#!/usr/bin/python

import random, MillerRabin, Arithmetic
from random import randrange, getrandbits
from itertools import repeat
from functools import reduce


flag = 'L4rG3_3xp0n3nt_15_b4D'

def getPrimePair(bits=512):
    '''
    genera un par de primos p , q con 
        p de nbits y
        p < q < 2p
    '''
    
    assert bits%4==0
    
    p = MillerRabin.gen_prime(bits)
    q = MillerRabin.gen_prime_range(p+1, 2*p)
    
    return p,q

def generateKeys(nbits=1024):
    '''
    Generates a key pair
        public = (e,n)
        private = d 
    such that
        n is nbits long
        (e,n) is vulnerable to the Wiener Continued Fraction Attack
    '''
    # nbits >= 1024 is recommended
    assert nbits%4==0
    
    p,q = getPrimePair(nbits//2)
    n = p*q
    phi = Arithmetic.totient(p, q)
        
    # generate a d such that:
    #     (d,n) = 1
    #    36d^4 < n
    good_d = False
    while not good_d:
        d = random.getrandbits(nbits//4)
        if (Arithmetic.gcd(d,phi) == 1 and 36*pow(d,4) < n):
            good_d = True
                    
    e = Arithmetic.modInverse(d,phi)
    return e,n,d

def rsa(M, key_ed, n):
  return_data = 1 
  M = M % n
  
  while key_ed != 0:
    if key_ed % 2 == 1:
      return_data = (return_data * M) % n      
    M = (M * M) % n
    key_ed = key_ed / 2

  return return_data

def main():
	e, n, d = generateKeys()
	print("e: ", e)
	print("n: ", n)
	print('What is d?')
	user_d = raw_input()
	if (str(d) == str(user_d)):
		print("Wow! You have Talent. \nI bestow you this flag, may it help you.")
		print(flag)
	else:
		print("Try again!")
main()

