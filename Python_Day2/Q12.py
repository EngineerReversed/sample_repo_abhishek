age =int(raw_input("Enter dog's age in human years"))
if age<=2:
    print("The dog's age in dog's years is %f"%(age*10.5))
else:
    print("The dog's age in dog's years is %f"%(2*10.5+(age-2)*4))
