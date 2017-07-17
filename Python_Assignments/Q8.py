r= int(raw_input("Enter matrix size "))
c= int(raw_input("Enter matrix size "))

if r<=2 and c<=2:
    print("Please enter matrix size greater than 2 by 2")
for i in range(1,r+1):
    if i==1 or i==r:
        print('*'*c)
    elif r%2==0 and i==r/2:
        print('*'*(c-1))
    elif r%2!=0 and i==(r/2+1):
        print('*'*(c-1))
    else:
        print('*')
