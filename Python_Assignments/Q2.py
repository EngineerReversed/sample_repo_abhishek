inp = raw_input("Enter the choice\nFor Fahrenheit, press F\nFor Celsius, press C\n")
temp = int(raw_input("Enter the temperature "))
if inp=='F':
    print("Temperature in Celsius is %d"%((temp-32)*5/9))
elif inp=='C':
    print("Temperature in Fahreinheit is %d"%((temp*9/5)+32))
