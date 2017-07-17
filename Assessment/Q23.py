filename = 'shakya.txt'
s = raw_input('Enter the string')
with open(filename, 'a') as f:
    f.write(s)
