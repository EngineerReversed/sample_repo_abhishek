n1 =  int(raw_input("Enter the number"))
def powertwo(n):
        return n > 0 and (n & (n - 1)) == 0

print(powertwo(n1))
