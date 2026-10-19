import string
import timeit

VOWELS = set("aeiou")
LOWERCASE = set(string.ascii_lowercase)

def a(s):
    letters = set(s) & LOWERCASE
    vowels = len(letters & VOWELS)
    return vowels, len(letters) - vowels

s = input()
print(*a(s))
