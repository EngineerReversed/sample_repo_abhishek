dic= {}
n =int(raw_input("Enter the n"))
for i in range(1,n+1):
    dic[i]=i*i
    print(str(i)+' : '+str(dic[i])+','),
