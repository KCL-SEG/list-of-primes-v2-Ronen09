"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes must be greater than 0")
    list = []
    i = 2;
    while True:
        if check_prime(i):
            list.append(i)
        if len(list) == number_of_primes:
            return list
        i += 1
    return list

def check_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True