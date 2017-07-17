tpl=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in range(0,len(tpl)):
    if tpl[i]%2==0:
        li.append(tpl[i])

tp2=tuple(li)
print(tp2)
