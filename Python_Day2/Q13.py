import re
a = raw_input("Input the letter of alphabet ")
b = ['a','e','i','o','u']
if a.lower() in b:
    print('Vowel')
elif a.lower() not in b:
    print('Consonant')
else:
    print('Enter a character')
