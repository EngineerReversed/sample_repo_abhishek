r= int(raw_input("Enter matrix size "))
c= int(raw_input("Enter matrix size "))

if r<=4 or c<=4:
    print("Please enter matrix size greater than 4 by 4")
else:
    for i in range(1,r+1):
        if i==1 or i==r:
            print(' '+'*'*(c-2)+' ')
        elif r%2==0 and i==r/2:
            print('*'+' '+'*'*(c-2))
        elif r%2!=0 and i==(r/2+1):
            print('*'+' '+'*'*(c-2))
        elif i<=r/2:
            print('*')
        else:
            print('*'+' '*(c-2)+'*')
