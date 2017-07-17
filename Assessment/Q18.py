class lst(object):
    def __init__(self):
        self.li=[]
    def app(self,n):
        return self.li.append(n)
    def delt(self,m):
        return self.li.remove(m)
    def disp(self):
        print(self.li)   





obj=lst()
choice=1
while choice!=0:
   print("0. Exit")
   print("1. Add")
   print("2. Delete")
   print("3. Display")
   choice=int(input("Enter choice: "))
   if choice==1:
       n=int(input("Enter number to append: "))
       obj.app(n)
       print(obj.disp())
   elif choice==2:
       n=int(input("Enter number to remove: "))
       obj.delt(n)
       print(obj.disp())
   elif choice==3:
       print(obj.disp())
   elif choice==0:
       print("Exiting!")
   else:
       print("Invalid choice!!")

print()
