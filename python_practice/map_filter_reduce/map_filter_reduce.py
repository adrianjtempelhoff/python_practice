#!/usr/bin/python3

# Python program to demonstrate working
# of map, filter, reduce.

from functools import reduce
  
# Return double of n
def addition(n):
    return n + n


# function that filters vowels
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


print("Map:")
# We double all numbers using map()
numbers = (1, 2, 3, 4)
print(numbers)
print("x2")
result = map(addition, numbers)
print(list(result))
print("\n")


print("Filter:")
# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
print(letters)
filtered_vowels = filter(filter_vowels, letters)

print('The filtered vowels are:')
for vowel in filtered_vowels:
    print(vowel)
print("\n")


print("Reduce:")
#my_add(5, 5)
numbers = [0, 1, 2, 3, 4]
print(numbers)
reduce(my_add, numbers)



