from collections import Counter
s =raw_input("Enter the string from user")
print(Counter(s.split()).most_common())
