import logging
logging.basicConfig(filename="example.log",format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)
logging.info("started the process")


print("Enter the list")
a = [int(x) for x in raw_input().split(',')]
flag = True
try:
    int(a)
except ValueError:
    logging.error("sequence length too small")
for i in range(0,len(a)-2):
    if a[i]+a[i+1] != a[i+2]:
        flag = False
if flag==True:
    print("Additive sequence")
else:
    print("Not an additive sequence")

   logging.info('process finished')
