import logging
#--log=INFO

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logger=logging.getLogger(__name__)
logging.info('Start reading records')
records={'john':55, 'tom':66}
#logging.warning('Warning out!')
logging.debug('Records: %s',records)



class Calculator(object):
    def __init__(self,n1, n2):
        self.num1 =n1
        self.num2=n2

    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def mult(self):
        return self.num1*self.num2
    def div(self):
        return self.num1/self.num2
    def mod(self):
        return self.num1%self.num2



def menu():
    
    l = ["Select operation.","1.Add","2.Subtract","3.Multiply","4.Divide","5.Modulus"]
    for i in l:
        print(i)
    st='y';
    while(st=='y'):
        flag0=True
        while flag0:
            choice = input("Enter choice(1/2/3/4/5):")
            try:    
                choice=int(choice)
                flag0=False
            except ValueError:
                print("Please try again ")

        print(choice)    
        flag=True
        while flag:
            num1 = input("Enter first number: ")
            try:    
                num1=int(num1)
                flag=False
            except ValueError:
                print("Please try again ")

        flag1=True
        while flag1:
            num2 = input("Enter second number: ")
            try:
                num2=int(num2)
                flag1=False
            except ValueError:
                print("Please try again ")
        aObject = Calculator(num1,num2)
        if choice == 1:
            print(aObject.add())
        elif choice == 2:
            if num1>num2:
                print(aObject.sub())
            else:
                print("num2 is Greater than num1.Thus displayed result is mod of the difference:")
                print(abs(aObject.sub()))
        elif choice == 3:
            print(aObject.mult())
        elif choice == 4:
            if num2==0:
                print("y should not be zero")
            else:
                print(aObject.div())
        elif choice == 5:
            print(aObject.mod())
        else:
            print("Invalid input")
        st=str(input("choose to continue (y/n)):"))
menu()
