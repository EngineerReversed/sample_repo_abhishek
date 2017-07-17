import re
emailAddress = raw_input("Enter the string")
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print (r2.group(1))
