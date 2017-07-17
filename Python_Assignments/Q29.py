import sys
amt = 0
print("Enter the transaction log")
while True:
    string = raw_input()
    if not string:
        break
    try:
        string = str(string)
    except ValueError:
        print("Please enter correct transaction log in format")
    v = string.split(" ")
    op = v[0]
    money = int(v[1])
    if op=="D":
        amt+=money
    elif op=="W":
        amt-=money
    else:
        pass
print(amt)
