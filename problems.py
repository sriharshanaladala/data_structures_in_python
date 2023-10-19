# n=100
# num1=0
# num2=1
# nextnumber = num2
# count = 1
#
# while count <=10:
#     print(num1)
#     count+=1
#     num1, num2 = num2, nextnumber
#     nextnumber = num1+num2
# print()

#
# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True
#
# def concatenate_prime_digits(num):
#     num_str = str(num)
#     prime_digits = ""
#
#     for digit in num_str:
#         if is_prime(int(digit)):
#             prime_digits += digit
#
#     return prime_digits
#
# # Example usage:
# number = 123456789
# concatenated_primes = concatenate_prime_digits(number)
# print("Concatenated prime digits:", concatenated_primes)
#
# import math
#
# def perfectSqaure(n):
#     square_root = math.sqrt(n)
#     return((square_root - math.floor(square_root)) == 0)
# def isSunnyNumber(n):
#     if (perfectSqaure(n + 1)):
#         print(str(n) + " is a sunny number!")
#     else:
#         print(str(n) +  " is not a sunny number!")
#
# print("Enter a number to check for sunny number:")
# sunnyNumber = int(input())
# isSunnyNumber(sunnyNumber)

import numpy as np


def getSortedNumber(n):
    digits = [int(x) for x in str(n)]
    number = int(''.join(map(str, np.sort(digits))))
    return number



print(getSortedNumber(658721))
