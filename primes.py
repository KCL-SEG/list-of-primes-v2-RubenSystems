"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def check_prime(number: int): 
    for i in range(2, number): 
        if number % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError()

    primes = []
    current_number = 2
    while len(primes) < number_of_primes:
        if check_prime(current_number):
            primes.append(current_number)
        current_number += 1
    return primes



