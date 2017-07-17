n = raw_input("Enter the numbers").split(',')
print([int(x) for x in n])
print(tuple(int(x) for x in n))
