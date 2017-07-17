s = raw_input("Enter the string")
d={"Digits":0, "Letters":0}
for c in s:
    if c.isdigit():
        d["Digits"]+=1
    elif c.isalpha():
        d["Letters"]+=1
    else:
        pass
print "LETTERS", d["Letters"]
print "DIGITS", d["Digits"]
