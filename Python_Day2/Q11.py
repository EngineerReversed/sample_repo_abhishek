r= int(raw_input("Enter matrix size "))
c= int(raw_input("Enter matrix size "))
t=1
if c%2==0:
    print('Column size should be odd')
elif r<=5 and c<=5:
    print("Please enter matrix size greater than 5 by 5")
else:
    for i in range(1,r+1):
        if i>r/2:
            print('*'+' '*(c-2)+'*')
        #elif r%2==0 and i==r/2:
         #   print('*'+' '*(c/2-1)+'*'+' '*(c/2-1)+'*')
        #elif r%2!=0 and i==(r/2+1):
        #    print('*'+' '*(c/2-1)+'*'+' '*(c/2-1)+'*')
        elif i<=r/2:
            if r%2==0:
                for m in range(1,r/2):
                    print("*"+' '*(m-1)+'*'+' '*(c/2-m-t)+'*'+' '*(m-1)+'*')
                    t=t+2
            else:
                for m in range(1,r/2+1):
                    print("*"+' '*(m-1)+'*'+' '*(c/2-m-t)+'*'+' '*(m-1)+'*')
                    t=t+2
