import logging
#--log=INFO

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logger=logging.getLogger(__name__)
logging.info('Start reading records')
records={'john':55, 'tom':66}
#logging.warning('Warning out!')
logging.debug('Records: %s',records)
'''numeric_level = getattr(logging, loglevel.upper(),None)
if not isinstance(numeric_level,int):
    raise ValueError('Invalid log level: %s'%loglevel)
'''

def menu():
    l = ["Select operation.","1.Add","2.Subtract","3.Multiply","4.Divide","5.Modulus"]
    for i in l:
        print(i)
    st='y';
    while(st=='y'):
        flag0=True
        while flag0:
            choice = raw_input("Enter choice(1/2/3/4/5):")
            try:    
                choice=int(choice)
                flag0=False
            except ValueError:
                print("Please try again ")

        print choice    
        flag=True
        while flag:
            num1 = raw_input("Enter first number: ")
            try:    
                num1=int(num1)
                flag=False
            except ValueError:
                print("Please try again ")

        flag1=True
        while flag1:
            num2 = raw_input("Enter second number: ")
            try:
                num2=int(num2)
                flag1=False
            except ValueError:
                print("Please try again ")

        if choice == 1:
            print(num1+num2)
        elif choice == 2:
            if num1>num2:
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
