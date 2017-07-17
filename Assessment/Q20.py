from collections import Counter
s =raw_input("Enter the string from user")
t=Counter(s.split()).most_common()
print(sorted(t))
