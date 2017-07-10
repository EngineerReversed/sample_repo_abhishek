import sys
a=sys.argv[1].lower()
b=a[::-1]
print(a)
print(b)
if a is b:
    print ('Palindrome')
else:
    print ('Not Palindrome')
