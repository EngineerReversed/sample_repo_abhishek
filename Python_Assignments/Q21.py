s = raw_input("Enter the string")
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
