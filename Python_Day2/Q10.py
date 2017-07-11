r= int(raw_input("Enter matrix size "))
c= int(raw_input("Enter matrix size "))

if r<=2 or c<=2:
    print("Please enter matrix size greater than 2 by 2")
else:
    for i in range(1,r+1):
        if i==r:
            print('*'*c)
        else:
            print('*')

