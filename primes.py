"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


import ctypes
import os 
import subprocess
"""
def safe_include_impl(filename: str):
    if not os.path.isfile(filename):
        comp_command = f"gcc -shared primes.c -O3 -o {filename}"
        subprocess.call(comp_command.split(" "))
    return ctypes.cdll.LoadLibrary(filename)



_prime_impl = safe_include_impl("primes_impl.so")

def primes(number_of_primes: int) -> [int]:
    if (number_of_primes <= 0):
        raise ValueError()

    primes = []
    current_number = 2
    while (len(primes) < number_of_primes):
        if (_prime_impl.is_prime(current_number)):
            primes.append(current_number)
        current_number += 1

    return primes


"""

def is_prime(number: int) -> bool: 
    current: int = 2
    while current ** 2 <= number:
        if not (number % current): 
            return False
        current += 1
    return True


def primes(number_of_primes: int) -> [int]:
    prime_arr : [int] = []
    current_number : int = 2
    while len(prime_arr) < number_of_primes:
        if is_prime(current_number):
            prime_arr.append(current_number)
        current_number += 1
    return prime_arr






print(primes(10))







