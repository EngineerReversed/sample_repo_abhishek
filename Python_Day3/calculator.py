
def menu():
    l = ["Select operation.","1.Add","2.Subtract","3.Multiply","4.Divide","5.Modulus"]
    for i in l:
        print(i)
    st='y';
    while(st=='y'):
        choice = input("Enter choice(1/2/3/4/5):")
        print choice    
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        if choice == 1:
            print(num1+num2)
        elif choice == 2:
            if x>y:
                print(num1-num2)
            else:
                print("num2 is Greater than num1.Thus displayed result is mod of the difference:")
                print(num2-num1)
        elif choice == 3:
            print(num1*num2)
        elif choice == 4:
            if num2==0:
                print("y should not be zero")
            else:
                print(num1/num2)
        elif choice == 5:
            print(num1%num2)
        else:
            print("Invalid input")
        st=str(raw_input("choose to continue (y/n)):"))
menu()
