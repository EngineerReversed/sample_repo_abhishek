r= int(input("Enter matrix size "))
c= int(input("Enter matrix size "))
m=1
t=c-4
if c%2==0:
    print('Column size should be odd')
elif r<=5 and c<=5:
    print("Please enter matrix size greater than 5 by 5")
elif abs(r-c)>=2:
    print("Enter rows and columns with at most difference of 1 and column should be odd")
else:
    for i in range(1,r+1):
            if i==1:
                print('*'+' '*(c-2)+'*')
            elif i==int(r/2+1):
                print('*'+' '*int((c-3)/2) +'*'+' '*int((c-3)/2)+'*')
            elif i>(int(r/2+1)):
                print('*'+' '*(c-2)+'*')
            else:
                print("*"+' '*(m-1)+'*'+' '*t+'*'+' '*(m-1)+'*')
                m+=1
                t-=2     
     
